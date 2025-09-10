import os


def get_files_info(working_directory, directory="."):
    try:
        # create full path
        full_path = os.path.join(working_directory, directory)

        # get absolute paths for comparison
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        # check if path is within the working directory
        if not abs_full_path.startswith(abs_working_dir):
            return f"Error: cannot list {directory} as it is outside the permitted working directory"

        # check if path is a directory
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        # get directory contents
        entries = os.listdir(abs_full_path)
        # entries.sort()

        # build restult string
        result = []
        for entry in entries:
            entry_path = os.path.join(abs_full_path, entry)
            try:
                stat_info = os.stat(entry_path)
                file_size = stat_info.st_size
                is_dir = os.path.isdir(entry_path)
                result.append(
                    f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}"
                )
            except OSError as e:
                return f"Error: Cannot access file '{entry}': {str(e)}"

        return "\n".join(result)

    except OSError as e:
        return f"Error: {str(e)}:working"
