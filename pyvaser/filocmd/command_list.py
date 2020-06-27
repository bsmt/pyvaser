from enum import IntEnum


class FiloCommandNumber(IntEnum):
    '''The "magic" bytes for each message'''
    RX_STD_MESSAGE                   = 0x0c  # done
    TX_STD_MESSAGE                   = 0x0d  # done
    RX_EXT_MESSAGE                   = 0x0e  # done
    TX_EXT_MESSAGE                   = 0x0f  # done
    SET_BUSPARAMS_REQ                = 0x10  # done
    GET_BUSPARAMS_REQ                = 0x11  # done
    GET_BUSPARAMS_RESP               = 0x12  # done
    GET_CHIP_STATE_REQ               = 0x13  # done
    CHIP_STATE_EVENT                 = 0x14  # done
    SET_DRIVERMODE_REQ               = 0x15  # done
    GET_DRIVERMODE_REQ               = 0x16  # done
    GET_DRIVERMODE_RESP              = 0x17  # done
    RESET_CHIP_REQ                   = 0x18
    RESET_CARD_REQ                   = 0x19
    START_CHIP_REQ                   = 0x1a  # done
    START_CHIP_RESP                  = 0x1b  # done
    STOP_CHIP_REQ                    = 0x1c  # done
    STOP_CHIP_RESP                   = 0x1d  # done
    READ_CLOCK_REQ                   = 0x1e
    READ_CLOCK_RESP                  = 0x1f
    GET_CARD_INFO_2                  = 0x20  # done
    # 33 (0x21) may be used
    GET_CARD_INFO_REQ                = 0x22  # done
    GET_CARD_INFO_RESP               = 0x23  # done
    GET_INTERFACE_INFO_REQ           = 0x24
    GET_INTERFACE_INFO_RESP          = 0x25
    GET_SOFTWARE_INFO_REQ            = 0x26  # done
    GET_SOFTWARE_INFO_RESP           = 0x27  # done
    GET_BUSLOAD_REQ                  = 0x28  # done
    GET_BUSLOAD_RESP                 = 0x29  # done
    RESET_STATISTICS                 = 0x2a
    CHECK_LICENSE_REQ                = 0x2b  # done
    CHECK_LICENSE_RESP               = 0x2c  # done
    CMD_ERROR_EVENT                  = 0x2d
    # 46 (0x2e) reserved
    # 47 (0x2f) reserved
    FLUSH_QUEUE                      = 0x30
    RESET_ERROR_COUNTER              = 0x31
    TX_ACK                           = 0x32  # done
    CAN_ERROR_EVENT                  = 0x33

    MEMO_GET_DATA                    = 0x34
    MEMO_PUT_DATA                    = 0x35
    MEMO_PUT_DATA_START              = 0x36
    MEMO_ASYNCOP_START               = 0x37
    MEMO_ASYNCOP_GET_DATA            = 0x38
    MEMO_ASYNCOP_CANCEL              = 0x39
    MEMO_ASYNCIO_FINISHED            = 0x3a
    DISK_FULL_INFO                   = 0x3b
    TX_REQ                           = 0x3c  # done
    SET_HEARTBEAT_RATE_REQ           = 0x3d
    HEARTBEAT_RESP                   = 0x3e
    SET_AUTO_TX_BUFFER               = 0x3f
    GET_EXTENDED_INFO                = 0x40
    TCP_KEEPALIVE                    = 0x41
    TX_INTERVAL_REQ                  = 0x42
    TX_INTERVAL_RESP                 = 0x43
    FILO_FLUSH_QUEUE_RESP            = 0x44
    # 69-72 (0x45-0x48) can be reused. (they put something at 0x48 anyways)
    # this is what's in the original source /shrug VVV
    AUTO_TX_BUFFER_REQ               = 0x48      # <<<
    AUTO_TX_BUFFER_RESP              = 0x49
    SET_TRANSCEIVER_MODE_REQ         = 0x4a
    TREF_SOFNR                       = 0x4b  # done
    SOFTSYNC_ONOFF                   = 0x4c  # done
    USB_THROTTLE                     = 0x4d  # done
    SOUND                            = 0x4e  # done
    LOG_TRIG_STARTUP                 = 0x4f
    SELF_TEST_REQ                    = 0x50
    SELF_TEST_RESP                   = 0x51
    USB_THROTTLE_SCALED              = 0x52  # done
    # 83-85 (0x53-0x55) can be reused
    SET_IO_PORTS_REQ                 = 0x56
    GET_IO_PORTS_REQ                 = 0x57
    GET_IO_PORTS_RESP                = 0x58
    # 89-94 (0x59-5e) can be used
    GET_CAPABILITIES_REQ             = 0x5f  # done
    GET_CAPABILITIES_RESP            = 0x60  # done
    GET_TRANSCEIVER_INFO_REQ         = 0x61  # done
    GET_TRANSCEIVER_INFO_RESP        = 0x62  # done
    MEMO_CONFIG_MODE                 = 0x63
    # 100 (0x64) can be used
    LED_ACTION_REQ                   = 0x65
    LED_ACTION_RESP                  = 0x66
    INTERNAL_DUMMY                   = 0x67
    READ_USER_PARAMETER              = 0x68  # done, asterisk
    MEMO_CPLD_PRG                    = 0x69
    LOG_MESSAGE                      = 0x6a  # done
    LOG_TRIG                         = 0x6b
    LOG_RTC_TIME                     = 0x6c

    SCRIPT_ENVVAR_CTRL_REQ           = 0x6d
    SCRIPT_ENVVAR_CTRL_RESP          = 0x6e

    SCRIPT_ENVVAR_TRANSFER_CTRL_REQ  = 0x6f
    SCRIPT_ENVVAR_TRANSFER_CTRL_RESP = 0x70
    SCRIPT_ENVVAR_TRANSFER_BULK      = 0x71

    SCRIPT_CTRL_REQ                  = 0x74
    SCRIPT_CTRL_RESP                 = 0x75

    SCRIPT_ENVVAR_NOTIFY_EVENT       = 0x76
    GET_DEVICE_NAME_REQ              = 0x77  # done
    GET_DEVICE_NAME_RESP             = 0x78  # done

    PING_REQ                         = 0x79
    PING_RESP                        = 0x7a

    SET_UNLOCK_CODE                  = 0x7b
    WRITE_USER_PARAMETER             = 0x7c
    CONFUSED_RESP                    = 0x7d


