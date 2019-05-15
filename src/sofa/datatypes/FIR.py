# Copyright (c) 2019 Jannika Lossner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from .base import _Base
from . import dimensions

from .. import access

class FIR(_Base):
    @property
    def IR(self): 
        """:class:`sofa.ArrayVariable` for the impulse response"""
        return access.ArrayVariable(self.database.dataset, "Data.IR")
    @property
    def SamplingRate(self): 
        """:class:`sofa.ScalarVariable` for the sampling rate"""
        return access.ScalarVariable(self.database.dataset, "Data.SamplingRate")
    @property
    def Delay(self): 
        """:class:`sofa.ArrayVariable` for the impulse response delay"""
        return access.ArrayVariable(self.database.dataset, "Data.Delay")
        
    def initialize(self, sample_count, delay_varies, string_length = 0):
        """Create the necessary variables and attributes
        
        Parameters
        ----------
        sample_count : int
            Number of samples per measurement
        delay_varies : bool
            Whether the Delay is varies between measurements
        string_length : int, optional
            Size of the longest data string
        """
        _Base._initialize_dimensions(self, sample_count, string_length = string_length)
        default_values = self.database._convention.default_data

        self.IR.initialize(dimensions.Definitions.DataValues(self.Type))
        if default_values["IR"] != 0: self.IR.set_values(default_values["IR"])
        self.SamplingRate.initialize()
        self.SamplingRate.set_value(default_values["SamplingRate"])
        self.SamplingRate.Units = dimensions.default_units["frequency"]
        self.Delay.initialize(dimensions.Definitions.DataDelay(self.Type, delay_varies))
        if default_values["Delay"] != 0: self.Delay.set_values(default_values["Delay"])
        return    

