"""
Node template for creating custom nodes.
"""

from typing import Any, Dict

from peekingduck.pipeline.nodes.abstract_node import AbstractNode





class Node(AbstractNode):
    """This is a template class of how to write a node for PeekingDuck.
    Args:
        config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
    """

    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)

        # initialize/load any configs and models here
        # configs can be called by self.<config_name> e.g. self.filepath
        # self.logger.info(f"model loaded with configs: config")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
        """This node does ___.
        Args:
            inputs (dict): Dictionary with keys "__", "__".
        Returns:
            outputs (dict): Dictionary with keys "__".
        """
        data_pool = list(inputs.keys())
        if "obj_person_onscreen" not in data_pool and "loop_count" not in data_pool:
            obj_person_onscreen = []
            loop_count = 0
        else:
            obj_person_onscreen = inputs["obj_person_onscreen"]
            loop_count = inputs["loop_count"]

        if "counter" not in data_pool: #a counter used to achieve time.sleep effect
            counter = 0
        else:
            counter = inputs["counter"]

        if "prev_coord" not in data_pool:
            prev_coord = (0,0)
        else:
            prev_coord = inputs["prev_coord"]

        if "prev_displacements" not in data_pool:
            prev_displacements = []
        else:
            prev_displacements = inputs["prev_displacements"]

        if "prev_safe" not in data_pool:
            prev_safe = []
        else:
            prev_safe = inputs["prev_safe"]

        if "obj_blocked_by_hand" not in data_pool:
            obj_blocked_by_hand = 'Not defined'
        else:
            obj_blocked_by_hand = inputs["obj_blocked_by_hand"]

        if "activate_detection" not in data_pool:
            activate_detection = False
        else:
            activate_detection = inputs["activate_detection"]

        if "dist3d" not in data_pool:
            dist3d = -1
        else:
            dist3d = inputs["dist3d"]

        if "obj_hand_interference_hist" not in data_pool:
            obj_hand_interference_hist = []
        else:
            obj_hand_interference_hist = inputs["obj_hand_interference_hist"]

        if "initial_area" not in data_pool:
            initial_area = 0
        else:
            initial_area = inputs["initial_area"]

        if "prev_area" not in data_pool:
            prev_area = []
        else:
            prev_area = inputs["prev_area"]

        if "area_shrunk_hist" not in data_pool:
            area_shrunk_hist = []
        else:
            area_shrunk_hist = inputs["area_shrunk_hist"]

        if "obj_is_close" not in data_pool:
            obj_is_close = False
        else:
            obj_is_close = inputs["obj_is_close"]

        outputs = {"obj_person_onscreen":obj_person_onscreen,
        "loop_count":loop_count,
        "counter":counter,
        "prev_coord":prev_coord,
        "prev_displacements":prev_displacements,
        "prev_safe":prev_safe,
        "obj_blocked_by_hand":obj_blocked_by_hand,
        'activate_detection':activate_detection,
        "dist3d":dist3d,
        "obj_hand_interference_hist":obj_hand_interference_hist,
        "prev_area":prev_area,
        "initial_area":initial_area,
        "area_shrunk_hist":area_shrunk_hist,
        "obj_is_close":obj_is_close}
        # result = do_something(inputs["in1"], inputs["in2"])
        # outputs = {"out1": result}
        # return outputs
        return outputs