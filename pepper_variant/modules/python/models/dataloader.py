from os.path import isfile, join
from os import listdir
from torch.utils.data import Dataset
import torchvision.transforms as transforms
import h5py
import sys


def get_file_paths_from_directory(directory_path):
    """
    Returns all paths of files given a directory path
    :param directory_path: Path to the directory
    :return: A list of paths of files
    """
    file_paths = [join(directory_path, file) for file in listdir(directory_path) if isfile(join(directory_path, file))
                  and file[-3:] == 'hdf']
    return file_paths


class SequenceDataset(Dataset):
    """
    Arguments:
        A HDF5 file path
    """
    def __init__(self, image_directory):
        self.transform = transforms.Compose([transforms.ToTensor()])
        file_image_pair = []

        hdf_files = get_file_paths_from_directory(image_directory)

        for hdf5_file_path in hdf_files:
            with h5py.File(hdf5_file_path, 'r') as hdf5_file:
                if 'summaries' in hdf5_file:
                    image_names = list(hdf5_file['summaries'].keys())
                    for image_name in image_names:
                        file_image_pair.append((hdf5_file_path, image_name))
                else:
                    sys.stderr.write("WARN: NO IMAGES FOUND IN FILE: " + hdf5_file_path + "\n")

        self.all_images = file_image_pair

    def __getitem__(self, index):
        # load the image
        hdf5_filepath, image_name = self.all_images[index]

        with h5py.File(hdf5_filepath, 'r') as hdf5_file:
            image = hdf5_file['summaries'][image_name]['image'][()]
            label = hdf5_file['summaries'][image_name]['label'][()]

        return image, label

    def __len__(self):
        return len(self.all_images)


class SequenceDatasetHP(Dataset):
    """
    Arguments:
        A HDF5 file path
    """
    def __init__(self, image_directory):
        self.transform = transforms.Compose([transforms.ToTensor()])
        file_image_pair = []

        hdf_files = get_file_paths_from_directory(image_directory)

        for hdf5_file_path in hdf_files:
            with h5py.File(hdf5_file_path, 'r') as hdf5_file:
                if 'summaries' in hdf5_file:
                    image_names = list(hdf5_file['summaries'].keys())

                    for image_name in image_names:
                        # for hp_tag 1
                        file_image_pair.append((hdf5_file_path, image_name, 1))
                        # for hp_tag 2
                        file_image_pair.append((hdf5_file_path, image_name, 2))
                else:
                    sys.stderr.write("WARN: NO IMAGES FOUND IN FILE: " + hdf5_file_path + "\n")

        self.all_images = file_image_pair

    def __getitem__(self, index):
        # load the image
        hdf5_filepath, image_name, hp_tag = self.all_images[index]

        with h5py.File(hdf5_filepath, 'r') as hdf5_file:
            if hp_tag == 1:
                image = hdf5_file['summaries'][image_name]['image_hp1'][()]
                label = hdf5_file['summaries'][image_name]['label_hp1'][()]
            else:
                image = hdf5_file['summaries'][image_name]['image_hp2'][()]
                label = hdf5_file['summaries'][image_name]['label_hp2'][()]

        return image, label

    def __len__(self):
        return len(self.all_images)