import zipfile as zp
import pathlib as pt


def make_archive(filepaths, dest_dir):
    dest_path = pt.Path(dest_dir, "compressed.zip")
    with zp.ZipFile(dest_path, 'w') as archive:

        for filepath in filepaths:
            filepath = pt.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_archive(archivepath, dest_dir):
    with zp.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)
