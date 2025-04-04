def generate_address(pulse_id: int) -> str:
    base = 13
    octet_range = range(-base, base + 1)  # -13 to 13 inclusive
    octets = []
    remaining = pulse_id

    for _ in range(4):
        val = (remaining % (2 * base + 1)) - base
        octets.append(str(val))
        remaining = remaining // (2 * base + 1)

    return '.'.join(octets[::-1])  # highest to lowest

def parse_address(address: str) -> int:
    parts = address.split('.')
    base = 13
    pulse_id = 0

    for part in parts:
        pulse_id = pulse_id * (2 * base + 1) + (int(part) + base)

    return pulse_id
