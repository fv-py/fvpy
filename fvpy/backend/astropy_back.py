from astropy.io import fits
from astropy.io.registry import IORegistryError
from astropy.table import Table

__all__ = ["ReadFile"]


class ReadFile:
    """Read a file and return a HDUList or Table object.

    If the file is a FITS file, return a HDUList object.
    If the file is a table file, return a Table object.
    If the file is neither a FITS file nor a table file, return None.

    Parameters
    ----------
    filename : str
        The filename of the file to be read.
    """

    def __init__(self, filename):
        self.hdulist = None
        self.table = None
        self.filename = filename

    def check_readable(self):
        """Check if the file is readable.

        Try to first open the file with ~`astropy.io.fits.open`.
        If it succeeds, set the attribute `hdulist` to `~astro.io.fits.HDUList`.
        If it fails, try to read the file with ~`astropy.table.Table.read`.
        If it succeeds, set the attribute `table` to `~astropy.table.Table`.
        If both fail, return None.
        """
        try:
            self.hdulist = fits.open(self.filename)
            return self.hdulist
        except OSError:
            self.hdulist = None
        try:
            self.table = Table.read(self.filename)
            return self.table
        except IORegistryError:
            self.table = None
            return None
