import struct
from enum import IntEnum

from pyvaser.filocmd.command_list import FiloCommandNumber
from pyvaser.filocmd.command import Command

'''
//Sub commands in CMD_GET_CAPABILITIES_REQ
#define CAP_SUB_CMD_DUMMY_NOT_IMPLEMENTED      0
#define CAP_SUB_CMD_DUMMY_UNAVAILABLE          1
#define CAP_SUB_CMD_SILENT_MODE                2
#define CAP_SUB_CMD_ERRFRAME                   3
#define CAP_SUB_CMD_BUS_STATS                  4
#define CAP_SUB_CMD_ERRCOUNT_READ              5
#define CAP_SUB_CMD_SINGLE_SHOT                6
#define CAP_SUB_CMD_SYNC_TX_FLUSH              7
#define CAP_SUB_CMD_HAS_LOGGER                 8
#define CAP_SUB_CMD_HAS_REMOTE                 9
#define CAP_SUB_CMD_HAS_SCRIPT                10

// the following are not capabilities/bits
#define CAP_SUB_CMD_DATA_START               1024
#define CAP_SUB_CMD_GET_LOGGER_INFO          CAP_SUB_CMD_DATA_START+1
#define CAP_SUB_CMD_REMOTE_INFO              CAP_SUB_CMD_DATA_START+2
#define CAP_SUB_CMD_HW_STATUS                CAP_SUB_CMD_DATA_START+3 // only used in hydra
#define CAP_SUB_CMD_FEATURE_EAN              CAP_SUB_CMD_DATA_START+4 // only used in hydra

// CAP_SUB_CMD_GET_LOGGER_TYPE
#define LOGGERTYPE_NOT_A_LOGGER 0
#define LOGGERTYPE_V1 1

// CAP_SUB_CMD_REMOTE_TYPE
#define REMOTE_TYPE_NOT_REMOTE  0
#define REMOTE_TYPE_WLAN 1
#define REMOTE_TYPE_LAN  2

typedef union {
  uint16_t padding;
  uint16_t channel;
} capExtraInfo_u;

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint16_t pad;
  uint16_t subCmdNo;
  capExtraInfo_u  subData;
} cmdCapabilitiesReq;

typedef struct
{
  uint32_t mask;
  uint32_t value;
} channelCap32_t;


typedef struct
{
  uint32_t     webServer;
  uint32_t     remoteType;
} RemoteInfo_t;

typedef struct
{
  uint32_t data;
} Info_t;

//Status codes in CMD_GET_CAPABILITIES_RESP
#define CAP_STATUS_OK                          0
#define CAP_STATUS_NOT_IMPLEMENTED             1
#define CAP_STATUS_UNAVAILABLE                 2

typedef struct {
  uint8_t  cmdLen;
  uint8_t  cmdNo;
  uint16_t pad;
  uint16_t subCmdNo;
  uint16_t status;
  union {
    channelCap32_t silentMode;     // CAP_SUB_CMD_SILENT_MODE
    channelCap32_t errframeCap;    // CAP_SUB_CMD_ERRFRAME
    channelCap32_t busstatCap;     // CAP_SUB_CMD_BUS_STATS
    channelCap32_t errcountCap;    // CAP_SUB_CMD_ERRCOUNT_READ
    channelCap32_t syncTxFlushCap; // CAP_SUB_CMD_SYNC_TX_FLUSH
    channelCap32_t loggerCap;     // CAP_SUB_CMD_HAS_LOGGER
    channelCap32_t remoteCap;     // CAP_SUB_CMD_HAS_REMOTE
    channelCap32_t scriptCap;     // CAP_SUB_CMD_HAS_SCRIPT
    Info_t loggerType;            // CAP_SUB_CMD_GET_LOGGER_TYPE
    RemoteInfo_t remoteInfo;      // CAP_SUB_CMD_REMOTE_TYPE
  };
} cmdCapabilitiesResp;
'''


class CommandCapabilitiesReq(Command):  # 0x5f
    cmd_len = 8
    cmd_num = FiloCommandNumber.GET_CAPABILITIES_REQ
    fmt = "< H H H H"

    def __init__(self, pad1, subcommand_number, pad2, channel):
        self.pad1 = pad1
        self.subcommand_number = subcommand_number
        self.pad2 = pad2
        self.channel = channel

    def serialize_body(self):
        return struct.pack(self.fmt, self.pad1, self.subcommand_number,
                           self.pad2, self.channel)


# Command capabilities status codes
class CapabilitiesStatus(IntEnum):
    OK = 0
    NOT_IMPLEMENTED = 1
    UNAVAILABLE = 2

# Command capabilities subcommands
class CapabilitiesSubcommand(IntEnum):
    DUMMY_NOT_IMPLEMENTED = 0
    DUMMY_UNAVAILABLE = 1
    SILENT_MODE = 2
    ERRFRAME = 3
    BUS_STATS = 4
    ERRCOUNT_READ = 5
    SINGLE_SHOT = 6
    SYNC_TX_FLUSH = 7
    HAS_LOGGER = 8
    HAS_REMOTE = 9
    HAS_SCRIPT = 10

    DATA_START = 1024
    GET_LOGGER_INFO = 1025
    REMOTE_INFO = 1026
    HW_STATUS = 1027
    FEATURE_EAN = 1028


class LoggerTypeSubcommand(IntEnum):
    NOT_A_LOGGER = 0
    V1 = 1


class RemoteTypeSubcommand(IntEnum):
    NOT_REMOTE = 0
    WLAN = 1
    LAN = 2


class ChannelCapability(object):
    cmd_len = 8
    fmt = "< I I"

    @classmethod
    def parse(cls, data, subcommand_number):
        (mask, val) = struct.unpack(self.fmt, data)
        return cls(subcommand_number, mask, val)

    def __init__(self, subcommand_number, mask, value):
        self.subcommand_number = subcommand_number
        self.mask = mask
        self.value = value

    def serialize_body(self):
        return struct.pack(self.fmt, self.mask, self.value)


class Info(object):  # LoggerTypeSubcommand
    cmd_len = 8
    fmt = "< I I"

    @classmethod
    def parse(cls, data, subcommand_number):
        (_data, pad) = struct.unpack(self.fmt, data)
        return cls(subcommand_number, _data, pad)

    def __init__(self, subcommand_number, data, pad):
        self.subcommand_number = subcommand_number
        self.data = data
        self.pad = pad

    def serialize_body(self):
        return struct.pack(self.fmt, self.data, self.pad)


class RemoteInfo(object):  # RemoteTypeSubcommand
    cmd_len = 8
    fmt = "< I I"

    @classmethod
    def parse(cls, data, subcommand_number):
        (server, remote_type) = struct.unpack(self.fmt, data)
        return cls(subcommand_number, server, remote_type)

    def __init__(self, subcommand_number, web_server, remote_type):
        self.subcommand_number = subcommand_number
        self.web_server = web_server
        self.remote_type = remote_type

    def serialize_body(self):
        return struct.pack(self.fmt, self.web_server, self.remote_type)


class CommandCapabilitiesResp(Command):  # 0x60
    cmd_len = 16
    cmd_num = FiloCommandNumber.GET_CAPABILITIES_RESP
    fmt_header = "< H H H"

    @classmethod
    def parse(cls, data):
        (pad, subcmd, status) = struct.unpack(self.fmt_header, data[0:6])
        sub_data = data[6:]

        if subcmd == CapabilitiesSubcommand.SILENT_MODE:
            command = ChannelCapability.parse(sub_data, subcmd)
        elif subcmd == CapabilitiesSubcommand.ERRFRAME:
            command = ChannelCapability.parse(sub_data, subcmd)
        elif subcmd == CapabilitiesSubcommand.BUS_STATS:
            command = ChannelCapability.parse(sub_data, subcmd)
        elif subcmd == CapabilitiesSubcommand.ERRCOUNT_READ:
            command = ChannelCapability.parse(sub_data, subcmd)
        elif subcmd == CapabilitiesSubcommand.SYNC_TX_FLUSH:
            command = ChannelCapability.parse(sub_data, subcmd)
        elif subcmd == CapabilitiesSubcommand.HAS_LOGGER:
            command = ChannelCapability.parse(sub_data, subcmd)
        elif subcmd == CapabilitiesSubcommand.HAS_REMOTE:
            command = ChannelCapability.parse(sub_data, subcmd)
        elif subcmd == CapabilitiesSubcommand.HAS_SCRIPT:
            command = ChannelCapability.parse(sub_data, subcmd)
        # TODO: find the other subcommands for Info and Remote

        return cls(pad, status, command)

    def __init__(self, pad, status, subcommand):
        self.pad = pad
        self.status = status
        self.subcommand = subcommand

    def serialize_body(self):
        header = struct.pack(self.fmt_header, self.pad,
                             self.subcommand.subcommand_number, self.status)
        subcmd = self.subcommand.serialize_body()
        return header + subcmd
