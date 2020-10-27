import os

img_formats = [".jpg", ".jpeg", ".png", ".JPEG", ".JPG", ".PNG"]
video_formats = [".mp4", ".MP4", ".avi", ".AVI"]


def _expand_user_and_relative_for_path(p):
    p = os.path.expanduser(p)
    return os.path.abspath(p)


def get_subfolders(folder_path):
    """Get immediate subfolders in folder_path

    Args:
        folder_path (str): target folder path

    Returns:
        list[str]: list of subfolder path string
    """
    folder_path = _expand_user_and_relative_for_path(folder_path)

    assert os.path.isdir(folder_path), "invalid folder path"
    return [f.path for f in os.scandir(folder_path) if f.is_dir()]


def get_subfolder_names(folder_path):
    """Get names of immediate subfolder in folder_path

    Args:
        folder_path (str): target folder path

    Returns:
        list[str]: list of subfolder name string
    """
    folder_path = _expand_user_and_relative_for_path(folder_path)
    assert os.path.isdir(folder_path), "invalid folder path"
    return [f.name for f in os.scandir(folder_path) if f.is_dir()]


def get_subfolders_recursively(folder_path):
    """Get all subfolders recursively in folder_path.

    Args:
        folder_path (str): target folder path

    Returns:
        list[str]: list of subfolder path string
    """
    folder_path = _expand_user_and_relative_for_path(folder_path)
    assert os.path.isdir(folder_path), "invalid folder path"
    folder_list = []
    for root, dirs, _ in os.walk(folder_path):
        for one_dir in dirs:
            one_dir = os.path.join(root, one_dir)
            folder_list.append(one_dir)
    return folder_list


def get_files_in_dir(dir_path, formats):
    """Get all files just in directory of dir_path.

    Args:
        dir_path (str): target directory path
        formats (list[str]): file fomates

    Returns:
        list[str]: list of file path string
    """
    dir_path = _expand_user_and_relative_for_path(dir_path)
    assert os.path.isdir(dir_path), "invalid directory path"
    assert len(formats), "invalid format"
    all_files = []
    files = os.listdir(dir_path)
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in formats:
            all_files.append(os.path.join(dir_path, f))
    return all_files


def get_files_recursively_in_dir(root, formats):
    """Get all files recursively contained in directory of root.

    Args:
        root (str): target directory
        formats (list[str]): file formats

    Returns:
        list[str]: list of file path string
    """
    root = _expand_user_and_relative_for_path(root)
    assert os.path.isdir(root), "invalid folder path"
    assert len(formats), "invalid format"
    all_files = []
    subfolders = get_subfolders_recursively(root)
    subfolders.append(root)
    for folder in subfolders:
        files = get_files_in_dir(folder, formats)
        all_files.extend(files)
    return all_files


def get_imgs_in_dir(root):
    """Get all imgs just in directory of root.

    Args:
        root (str): target directory

    Returns:
        list[str]: list of img path string
    """
    global img_formats
    return get_files_in_dir(root, img_formats)


def get_imgs_recursively_in_dir(root):
    """Get all imgs recursively contained in directory of root.

    Args:
        root (str): target directory

    Returns:
        list[str]: list of img path string
    """
    global img_formats
    return get_files_recursively_in_dir(root, img_formats)

