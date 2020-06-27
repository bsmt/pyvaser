// Format for arduino serial CAN messages:
// all values hex encoded
//<ID[4]><SPACE><DATA_LEN><SPACE><DATA[DATA_LEN * 2]>

#include <Canbus.h>
#include <defaults.h>
#include <global.h>
#include <mcp2515.h>
#include <mcp2515_defs.h>


void setup() {
  Serial.begin(115200);

  if (!Canbus.init(CANSPEED_500))
  {
    Serial.println("ERR: Can't init CAN");
  }

  Serial.println("Starting");
}

void loop() {
  checkForCANRx();
  checkForCANTx();
}


// check if we have a CAN bus message received,
// and repeat it out over our arduino serial to the test controller program
void checkForCANRx()
{
  tCAN message;
  if (mcp2515_check_message())
  {
    if (mcp2515_get_message(&message))
    {
      uint16_t can_id = message.id;
      Serial.print(can_id, HEX);
      Serial.print(" ");
      Serial.print(message.header.length, HEX);
      Serial.print(" ");
      for (int i = 0; i < message.header.length; i++)
      {
        Serial.print(message.data[i], HEX);
      }
      Serial.println("");
    }
  }
}

// see if we received a command from the controller, and send the data out
void checkForCANTx()
{
  tCAN message;

  if (Serial.available() == 0)
  {
    return;
  }

  String serial_buffer;
  serial_buffer = Serial.readString();

  message.id = strtol((String("0x") + serial_buffer.substring(0, 4)).c_str(), NULL, 16);
  message.header.rtr = 0;

  if (serial_buffer.charAt(4) != ' ')
  {
    Serial.print("ERR: Incorrect message format 1 ");
    Serial.print(serial_buffer.charAt(5));
    Serial.println("");
    return;
  }

  // read data size
  message.header.length = serial_buffer.substring(5,6).toInt();
  if (message.header.length > 8)
  {
    Serial.println("ERR: Data size is greater than 8 bytes");
    return;
  }
    
  if(serial_buffer.charAt(6) != ' ')
  {
    Serial.println("ERR: Incorrect message format 2");
    return;
  }

  // read actual bytes
  int end_idx = 7 + (message.header.length * 2);
  int i2 = 0;
  for (int i = 7; i < end_idx; i += 2)
  {
    message.data[i2] = strtol((String("0x") + serial_buffer.substring(i, i + 2)).c_str(), NULL, 16);
    i2++;
  }

  // send it out
  mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
  mcp2515_send_message(&message);
  Serial.println("Sent");
}
