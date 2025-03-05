#
# Autogenerated by Thrift Compiler (0.19.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def train_with_weights(self, training_file, initial_weights, load_probability, k, h, eta, epochs, scheduling_policy):
        """
        Parameters:
         - training_file
         - initial_weights
         - load_probability
         - k
         - h
         - eta
         - epochs
         - scheduling_policy

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def train_with_weights(self, training_file, initial_weights, load_probability, k, h, eta, epochs, scheduling_policy):
        """
        Parameters:
         - training_file
         - initial_weights
         - load_probability
         - k
         - h
         - eta
         - epochs
         - scheduling_policy

        """
        self.send_train_with_weights(training_file, initial_weights, load_probability, k, h, eta, epochs, scheduling_policy)
        return self.recv_train_with_weights()

    def send_train_with_weights(self, training_file, initial_weights, load_probability, k, h, eta, epochs, scheduling_policy):
        self._oprot.writeMessageBegin('train_with_weights', TMessageType.CALL, self._seqid)
        args = train_with_weights_args()
        args.training_file = training_file
        args.initial_weights = initial_weights
        args.load_probability = load_probability
        args.k = k
        args.h = h
        args.eta = eta
        args.epochs = epochs
        args.scheduling_policy = scheduling_policy
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_train_with_weights(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = train_with_weights_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "train_with_weights failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["train_with_weights"] = Processor.process_train_with_weights
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_train_with_weights(self, seqid, iprot, oprot):
        args = train_with_weights_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = train_with_weights_result()
        try:
            result.success = self._handler.train_with_weights(args.training_file, args.initial_weights, args.load_probability, args.k, args.h, args.eta, args.epochs, args.scheduling_policy)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("train_with_weights", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class train_with_weights_args(object):
    """
    Attributes:
     - training_file
     - initial_weights
     - load_probability
     - k
     - h
     - eta
     - epochs
     - scheduling_policy

    """


    def __init__(self, training_file=None, initial_weights=None, load_probability=None, k=None, h=None, eta=None, epochs=None, scheduling_policy=None,):
        self.training_file = training_file
        self.initial_weights = initial_weights
        self.load_probability = load_probability
        self.k = k
        self.h = h
        self.eta = eta
        self.epochs = epochs
        self.scheduling_policy = scheduling_policy

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.training_file = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.initial_weights = Weights()
                    self.initial_weights.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.load_probability = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.k = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.h = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.DOUBLE:
                    self.eta = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.epochs = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.scheduling_policy = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('train_with_weights_args')
        if self.training_file is not None:
            oprot.writeFieldBegin('training_file', TType.STRING, 1)
            oprot.writeString(self.training_file.encode('utf-8') if sys.version_info[0] == 2 else self.training_file)
            oprot.writeFieldEnd()
        if self.initial_weights is not None:
            oprot.writeFieldBegin('initial_weights', TType.STRUCT, 2)
            self.initial_weights.write(oprot)
            oprot.writeFieldEnd()
        if self.load_probability is not None:
            oprot.writeFieldBegin('load_probability', TType.DOUBLE, 3)
            oprot.writeDouble(self.load_probability)
            oprot.writeFieldEnd()
        if self.k is not None:
            oprot.writeFieldBegin('k', TType.I32, 4)
            oprot.writeI32(self.k)
            oprot.writeFieldEnd()
        if self.h is not None:
            oprot.writeFieldBegin('h', TType.I32, 5)
            oprot.writeI32(self.h)
            oprot.writeFieldEnd()
        if self.eta is not None:
            oprot.writeFieldBegin('eta', TType.DOUBLE, 6)
            oprot.writeDouble(self.eta)
            oprot.writeFieldEnd()
        if self.epochs is not None:
            oprot.writeFieldBegin('epochs', TType.I32, 7)
            oprot.writeI32(self.epochs)
            oprot.writeFieldEnd()
        if self.scheduling_policy is not None:
            oprot.writeFieldBegin('scheduling_policy', TType.I32, 8)
            oprot.writeI32(self.scheduling_policy)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(train_with_weights_args)
train_with_weights_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'training_file', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'initial_weights', [Weights, None], None, ),  # 2
    (3, TType.DOUBLE, 'load_probability', None, None, ),  # 3
    (4, TType.I32, 'k', None, None, ),  # 4
    (5, TType.I32, 'h', None, None, ),  # 5
    (6, TType.DOUBLE, 'eta', None, None, ),  # 6
    (7, TType.I32, 'epochs', None, None, ),  # 7
    (8, TType.I32, 'scheduling_policy', None, None, ),  # 8
)


class train_with_weights_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = TrainResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('train_with_weights_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(train_with_weights_result)
train_with_weights_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [TrainResult, None], None, ),  # 0
)
fix_spec(all_structs)
del all_structs
