# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-04 20:19:07

from base import baseConfig

class excelConfig(baseConfig):
    VARS_REQ = {'Name', 'Definition', 'Tags'}
    MI_REQ = {'Name', 'Expression', 'Label', 'Color', 'Tags'}
    """initializing a configuration file

    TODO:

    Args:
        tfile  :| baseConfig class
        tloc  ::| baseConfig class
        tsheet :| type(str)

    Attributes:
        tfile ::::| passing the name of the file to be read into
        tloc :::::| passing the absolute file path for the file
        tpath ::::| generating the file path from tloc and tfile
        is_valid :| determing if the file path was valid - returning bool
        filetype :| Excel file module
        tsheet :::| passing the name of the sheet in the excel file

    """

    def __init__(self, tfile, tloc, tsheet):
        super().__init__(tfile, tloc)
        self.filetype = 'Excel'
        self.tsheet = tsheet

        if self.is_valid:
            try:
                self.df = pd.read_excel(self.tpath, self.tsheet)
                self.fields = list(self.df.columns.values)
            except:
                self.df = None
                self.fields = []
        else:
            self.df = None
            self.fields = []

    def valid_var_stup(self):
        """method to determine if the excel file sheet is configured correctly
        for variables

        Notes:

        Args:

        Returns:
            True self.fields contains specified fields from VARS_REQ, False otherwise.

        """
        if VARS_REQ.issubset(self.fields):
            return True
        else:
            return False

    def valid_mi_stup(self):
        """method to determine if the excel file sheet is configured correctly
        for master items

        Note:

        Args:

        Returns:
            True self.fields contains specified fields from MI_REQ, False otherwise.
        """
        if MI_REQ.issubset(self.fields):
            return True
        else:
            return False
        
 # below: populating excel file information into a dictionary, named "values_dict"

    def config_to_dict(tfile): 
        
        excel_data = pd.read_excel(tfile) #read the excel file
        
        values_dict = excel_data.to_dict() #convert the excel file data to dictionary
