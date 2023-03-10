"""
Node template for creating custom nodes.
"""

from typing import Any, Dict
import threading, math
from pathlib import Path
import numpy as np

import winsound


from peekingduck.pipeline.nodes.abstract_node import AbstractNode
from peekingduck.pipeline.nodes.draw.utils.bbox import draw_bboxes




class Node(AbstractNode):
    """This is a template class of how to write a node for PeekingDuck.

    Args:
        config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
    """
    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)
        self.thread = None
        self.thread1 = None

    def playsound(self, freq, duration):
        if self.thread is None or not self.thread.is_alive():
            self.thread = threading.Thread(target=winsound.Beep, args=(freq, duration), daemon=True)
            self.thread.start()

    
    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
        """This node does ___.
        Args:
            inputs (dict): Dictionary with keys "__", "__".

        Returns:
            outputs (dict): Dictionary with keys "__".
        """
        bbox_labels = inputs["bbox_labels"]
        bbox_scores = inputs["bbox_scores"]
        obj_3D_locs = inputs["obj_3D_locs"]
        bboxes = inputs["bboxes"]
        
        obj_blocked_by_hand = inputs["obj_blocked_by_hand"]

        activate_detection = inputs['activate_detection']
        # activate_detection = False #for debug

        max_score_p = 0
        max_score_item = 0
        person_i = -1
        item_i = -1

        for i, x in enumerate(bbox_labels):
            if x == "person":
                if bbox_scores[i] > max_score_p:
                    max_score_p = bbox_scores[i]
                    person_i = i
            else:
                if bbox_scores[i] > max_score_item:
                    max_score_item = bbox_scores[i]
                    item_i = i
        
        if not activate_detection:
            pass
        elif person_i != -1:
            if item_i == -1:
                #only person on screen
                if obj_blocked_by_hand == True:
                    self.playsound(1100, 80)
                else:
                    self.playsound(300, 150)

            else:
                #both on screen
                freq = 500
                duration = 80
                #####TODO: change this freq based on distance

                #3d distance
                a = obj_3D_locs[person_i]
                b = obj_3D_locs[item_i]
                dist_3d = np.linalg.norm(a-b)
                # print('3d dist: ', dist_3d)

                #2d distance
                a = np.array(((bboxes[person_i][2] + bboxes[person_i][0])/2, (bboxes[person_i][3] + bboxes[person_i][1])/2))
                b = np.array(((bboxes[item_i][2] + bboxes[item_i][0])/2, (bboxes[item_i][3] + bboxes[item_i][1])/2))
                # print(a, b)
                dist2d = np.linalg.norm(a-b)
                # print(f'dist2d:{dist2d}')
                
                coefficient = round((dist2d)*(1+(math.log(dist_3d)-1)/2),3)
                duration = 80
                f_freq = math.floor(5000 * coefficient)
                # print(f_freq)
                f_freq = min(f_freq, 4500)
                f_freq = max(f_freq, 1100)
                self.playsound(f_freq, duration)

        elif item_i != -1:
            #only item on screen
            self.playsound(400, 150)


        #filter bboxes and labels
        if person_i != -1:
            if item_i != -1:
                n_bboxes = [bboxes[person_i], bboxes[item_i]]
                n_bbox_labels = [bbox_labels[person_i], bbox_labels[item_i]]
            else:
                n_bboxes = [bboxes[person_i]]
                n_bbox_labels = [bbox_labels[person_i]]
        elif item_i != -1:
            n_bboxes = [bboxes[item_i]]
            n_bbox_labels = [bbox_labels[item_i]]
        else:
            n_bboxes = []
            n_bbox_labels = []


        dist2d_centre = -1 #default

        if item_i != -1: #as long as item appears
            #2d distance from centre
            a = np.array(((bboxes[item_i][2] + bboxes[item_i][0])/2, (bboxes[item_i][3] + bboxes[item_i][1])/2))
            b = np.array((0.5, 0.5)) #center
            dist2d_centre = np.linalg.norm(a-b)
            # print(f'dist2d_centre:{dist2d_centre}')



        #draw bboxes
        draw_bboxes(
            inputs["img"], n_bboxes, n_bbox_labels, True
        )
        return {"n_bboxes": n_bboxes, 
        "n_bbox_labels":n_bbox_labels,
        "dist2d_centre":dist2d_centre
        }
