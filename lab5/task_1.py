#!/usr/local/bin/python3

excluded_codes = set({0x03A2, 0x03C2})
print("Greek alphabet [capital]");
for code in range(0x0391, 0x03AA):
  if not code in excluded_codes:
    print(chr(code), end=" ");
print();

print("Greek alphabet [small]");
for code in range(0x03B1, 0x03CA):
  if not code in excluded_codes:
    print(chr(code), end=" ");
print();
