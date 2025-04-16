# test_netgen.py
import unittest
from netgen import generate_interface_config

class TestNetgen(unittest.TestCase):
    def test_generate_interface_config(self):
        input_data = {
            "name": "GigabitEthernet0/1",
            "description": "Uplink to core switch",
            "ip_address": "10.0.0.1",
            "subnet_mask": "255.255.255.0"
        }

        expected_output = (
            "interface GigabitEthernet0/1\n"
            " description Uplink to core switch\n"
            " ip address 10.0.0.1 255.255.255.0\n"
            " no shutdown"
        )

        actual_output = generate_interface_config(input_data)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
