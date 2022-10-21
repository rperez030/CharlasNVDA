import os
import datetime as dt


class FileInfo:
    """Single file information.
    
    Attributes: filename, abspath, datetime
    Properties: size (read only)
    """
    
    def __init__(self, filename: str):
        if not os.path.isfile(filename):
            raise FileNotFoundError('"' + filename + '" does not exist or is not a file')
        # filename exists and is a file (not directory)
        self.filename = filename
        self.abspath = os.path.abspath(filename)
        self.basename = os.path.basename(self.abspath)
        self.datetime = self._get_datetime()
    
    def __repr__(self):
        return f"FileItem({self.filename})"
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return self.abspath
    
    def _get_datetime(self):
        """Obtain datetime object from last modified time of the file"""

        mtime = os.path.getmtime(self.abspath)  # last modified time (timestamp)
        return dt.datetime.fromtimestamp(mtime)
    
    @property
    def size(self):
        """Obtain size of the file in bytes"""
        
        if not hasattr(self, '_size'):
            self._size = os.path.getsize(self.abspath)  # cache calculated size
        return self._size
    
    @size.setter
    def size(self, value):
        """Avoid external modification of the attribute"""
        
        raise AttributeError("'size' attribute is read-only")
    
    def format_datetime(self, format:str = "%Y-%m-%d %H:%M:%S") -> str:
        """Format datetime for printing/exporting"""
        
        return self.datetime.strftime(format)


