"""This module include test of function process_data."""

import json
import pathlib

import pytest

from hw2 import process_data


def make_path(file_name):
    """Take a filename and returns path to filename.

    Args:
        file_name: name of file

    Returns:
        Returns full path to filename
    """
    return pathlib.Path(file_name)


TEST_PROCESS_DATA = (
    (make_path('data_hw2.json'),
     make_path('datas_output.json'),
     {'2012-12-24': 50.0, '2022-10-30': 50.0, 'gmail.com': 50.0, 'yandex.ru': 50.0},
     ),
    (make_path('data_hw1_2.json'),
     make_path('datas_test_output2.json'),
     {'2012-12-24': 33.33, '2019-10-30': 33.33, '2022-10-30': 33.33,
      'gmail.com': 33.33, 'mail.ru': 33.33, 'yandex.ru': 33.33,
      },
     ),
    (make_path('data_hw2_3.json'),
     make_path('datas_output3.json'), {},
     ),
)

TEST_ERROR_PROCESS_DATA = (
    ('/home/runner/work/homeworks_23/hw2/data.json',
     '/home/runner/work/homeworks_23/hw2/datas_output.json', 'Is not a file path',
     ),
    ('/home/runner/work/homeworks_23/hw2/data_hw2.json',
     '/home/runner/work/homeworks_23/hw2/data.json', 'Is not a file path',
     ),
)


@pytest.mark.parametrize('input_filepath,output_filepath,expected', TEST_PROCESS_DATA)
def test_process_data(input_filepath: str, output_filepath: str, expected: dict) -> None:
    """A function that tests process_data function.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file
        expected:  expected function output.
    """
    process_data(input_filepath, output_filepath)
    with open(output_filepath, 'r') as file1:
        input_file = json.load(file1)
    assert input_file == expected


@pytest.mark.parametrize('input_filepath,output_filepath,expected', TEST_ERROR_PROCESS_DATA)
def test_errors_process_data(input_filepath: str, output_filepath: str, expected: str) -> None:
    """A function that tests process_data function.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file
        expected:  expected function output.
    """
    try:
        process_data(input_filepath, output_filepath)
    except FileNotFoundError as err:
        assert expected == str(err)
