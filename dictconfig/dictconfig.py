import os
import json
import configparser as cp


def isfloat(string):
    """
    Checks if a string can be converted into a float.

    Parameters
    ----------
    value : str

    Returns
    -------
    bool:
        True/False if the string can/can not be converted into a float.

    """
    try:
        float(string)
        return True

    except ValueError:
        return False


def isint(string):
    """
    Checks if a string can be converted into an int.

    Parameters
    ----------
    value : str

    Returns
    -------
    bool:
        True/False if the string can/can not be converted into an int.

    """
    try:
        int(string)
        return True

    except ValueError:
        return False


def isbool(string):
    """
    Checks if a string can be converted into a boolean.

    Parameters
    ----------
    value : str

    Returns
    -------
    bool:
        True/False if the string can/can not be converted into a boolean.

    """
    return string in ("True", "true", "False", "false")


def islist(string):
    """
    Checks if a string can be converted into a list.

    Parameters
    ----------
    value : str

    Returns
    -------
    bool:
        True/False if the string can/can not be converted into a list.

    """
    return (list(string)[0] == "[") and (list(string)[-1] == "]")


def get_parameter(parameter, value, section, config):
    """
    Get an option value from a given section

    Parameters
    ----------
    parameter: str

    section: str

    config: configparser.ConfigParser

    Returns
    -------
    param: int, float, list or bool
        The
    """
    if isint(value):
        param = config.getint(section, parameter)
        print("Int")

    elif isfloat(value):
        param = config.getfloat(section, parameter)
        print("Float")

    elif isbool(value):
        param = config.getboolean(section, parameter)
        print("Bool")

    elif islist(value):
        param = json.loads(config.get(section, parameter))
        print("list")

    else:
        param = config.get(section, parameter)
        print("str")

    return param



def check_sections_exist(section, config):
    """

    Parameters
    ----------
    section: str or list or "All"
        The section name or list of section names to read from the
        parameter file. Default: "All"

    config:


    Returns
    -------
    section: list
        A list containing all the sections requested. If 'All' is specified
        then all the sections listen in the parameter file will be returned.
        If a single string is passed, the it will be converted to a single item
        list.

    """

    # If the sections are given as a list check that each name is valid.
    if isinstance(section, list):
        for section_name in section:
            if not config.has_section(section_name):
                msg = (f"'{section_name}' is not a section in the "
                "parameter file")
                raise ValueError(msg)

    # If 'All' sections are wanted get the list of sections in the param file
    elif isinstance(section, str):
        if section == "All":
            section = config.sections()

        else:
            if not config.has_section(section):
                msg = f"'{section}' is not a section in the parameter file"
                raise ValueError(msg)
            else:
                # Convert the single string into a list to enumerate later.
                section = [section]

    else:
        raise TypeError(f"Sections must be a string or a list of strings. "
                       "Instead section is type {type(section)}")

    return section

def read_params(param_path, section="All"):
    """
    Reads 

    Parameters
    ----------
    param_path : str
        The path to a parameter file that can be read using config parser.

    section : str or list or "All"
        The section name or list of section names to read from the
        parameter file. Default: "All"

    Returns
    -------
    params : dict
        A dictionary containing the parameters and values from the file.

    """
    
    if not os.path.exists(param_path):
        raise OSError(f"Could not find parameter file: {param_path}")

    params = {}

    config = cp.ConfigParser()
    config.read(param_path)

    section = check_sections_exist(section, config)

    for section_name in section:
        for key, value in zip(config[section_name].keys(), config[section_name].values()):
            #print(keys, value)
            params[key] = get_parameter(key, value, section_name, config)
            
    return params


if __name__ == "__main__":

    #config = cp.ConfigParser()
    #config.read("config.params")

    print(read_params("config.params", ["Section1", "Section3"]))

    #check_sections_exist(config, "Section2")
    #check_sections_exist(config, "Section3")
    #check_sections_exist(config, "All")
    #check_sections_exist(config, ["Section1", "Section3"])
    #check_sections_exist(config, ["Section1", "Section4"])



