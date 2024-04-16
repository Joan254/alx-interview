#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """Takes a list of lists and returns a boolean indicating
    whether all boxes in the list can be opened. A key with the same
    number as a box opens that box. You can assume all keys will be
    positive integers. There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Add the first box to the set of opened boxes
    opened_boxes.add(0)

    def unlock_boxes(box_index):
        """Function to recursively unlock boxes."""
        for key in boxes[box_index]:  # Iterate through keys in the current box

            # If the key opens a box that hasn't been opened yet
            if key < len(boxes) and key not in opened_boxes:
                # Mark the box as opened
                opened_boxes.add(key)
                # Recursively unlock the newly opened box
                unlock_boxes(key)

    # Start unlocking boxes from the first box
    unlock_boxes(0)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
