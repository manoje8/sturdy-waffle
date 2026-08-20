def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return target == root.val
    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)
