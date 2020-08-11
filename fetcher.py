import os


img_formats = [".jpg", ".jpeg", ".png", ".JPEG", ".JPG", ".PNG"]


def get_subfolders_recursively(folder_path):
    """Get all subfolders recursively in folder_path.
    """
    folder_list = []
    for root, dirs, _ in os.walk(folder_path):
        for one_dir in dirs:
            one_dir = os.path.join(root, one_dir)
            folder_list.append(one_dir)
    return folder_list


def get_files_in_dir(dir_path, formats):
    """Get all files just in directory of dir_path.
    """
    all_files = []
    files = os.listdir(dir_path)
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in formats:
            all_files.append(os.path.join(dir_path, f))
    return all_files


def get_files_recursively_in_dir(root, formats):
    """Get all files recursively contained in directory of root.
    """
    all_files = []
    subfolders = get_subfolders_recursively(root)
    subfolders.append(root)
    for folder in subfolders:
        files = get_files_in_dir(folder, formats)
        all_files.extend(files)
    return all_files


def get_imgs_in_dir(root):
    """Get all imgs just in directory of root.
    """
    return get_files_in_dir(root, img_formats)


def get_imgs_recursively_in_dir(root):
    """Get all imgs recursively contained in directory of root.
    """
    return get_files_recursively_in_dir(root, img_formats)
