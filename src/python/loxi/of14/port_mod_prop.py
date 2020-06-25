# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template module.py
# Do not modify

import struct
import loxi
from . import util
import loxi.generic_util

import sys
ofp = sys.modules['loxi.of14']

class port_mod_prop(loxi.OFObject):
    subtypes = {}


    def __init__(self, type=None):
        if type != None:
            self.type = type
        else:
            self.type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        subclass = port_mod_prop.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = port_mod_prop()
        obj.type = reader.read("!H")[0]
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.type != other.type: return False
        return True

    def pretty_print(self, q):
        q.text("port_mod_prop {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


class ethernet(port_mod_prop):
    type = 0

    def __init__(self, advertise=None):
        if advertise != None:
            self.advertise = advertise
        else:
            self.advertise = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.advertise))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = ethernet()
        _type = reader.read("!H")[0]
        assert(_type == 0)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        obj.advertise = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.advertise != other.advertise: return False
        return True

    def pretty_print(self, q):
        q.text("ethernet {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("advertise = ");
                q.text("%#x" % self.advertise)
            q.breakable()
        q.text('}')

port_mod_prop.subtypes[0] = ethernet

class experimenter(port_mod_prop):
    subtypes = {}

    type = 65535

    def __init__(self, experimenter=None, exp_type=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        if exp_type != None:
            self.exp_type = exp_type
        else:
            self.exp_type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 4)
        subclass = experimenter.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = experimenter()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        obj.experimenter = reader.read("!L")[0]
        obj.exp_type = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        if self.exp_type != other.exp_type: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("exp_type = ");
                q.text("%#x" % self.exp_type)
            q.breakable()
        q.text('}')

port_mod_prop.subtypes[65535] = experimenter

class optical(port_mod_prop):
    type = 1

    def __init__(self, configure=None, freq_ldma=None, fl_offset=None, grid_span=None, tx_pwr=None):
        if configure != None:
            self.configure = configure
        else:
            self.configure = 0
        if freq_ldma != None:
            self.freq_ldma = freq_ldma
        else:
            self.freq_ldma = 0
        if fl_offset != None:
            self.fl_offset = fl_offset
        else:
            self.fl_offset = 0
        if grid_span != None:
            self.grid_span = grid_span
        else:
            self.grid_span = 0
        if tx_pwr != None:
            self.tx_pwr = tx_pwr
        else:
            self.tx_pwr = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.configure))
        packed.append(struct.pack("!L", self.freq_ldma))
        packed.append(struct.pack("!L", self.fl_offset))
        packed.append(struct.pack("!L", self.grid_span))
        packed.append(struct.pack("!L", self.tx_pwr))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = optical()
        _type = reader.read("!H")[0]
        assert(_type == 1)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        obj.configure = reader.read("!L")[0]
        obj.freq_ldma = reader.read("!L")[0]
        obj.fl_offset = reader.read("!L")[0]
        obj.grid_span = reader.read("!L")[0]
        obj.tx_pwr = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.configure != other.configure: return False
        if self.freq_ldma != other.freq_ldma: return False
        if self.fl_offset != other.fl_offset: return False
        if self.grid_span != other.grid_span: return False
        if self.tx_pwr != other.tx_pwr: return False
        return True

    def pretty_print(self, q):
        q.text("optical {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("configure = ");
                q.text("%#x" % self.configure)
                q.text(","); q.breakable()
                q.text("freq_ldma = ");
                q.text("%#x" % self.freq_ldma)
                q.text(","); q.breakable()
                q.text("fl_offset = ");
                q.text("%#x" % self.fl_offset)
                q.text(","); q.breakable()
                q.text("grid_span = ");
                q.text("%#x" % self.grid_span)
                q.text(","); q.breakable()
                q.text("tx_pwr = ");
                q.text("%#x" % self.tx_pwr)
            q.breakable()
        q.text('}')

port_mod_prop.subtypes[1] = optical


