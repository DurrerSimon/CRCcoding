# TI-nspire CX II-T CRC Encoder and Decoder

This repository contains Python scripts for performing CRC (Cyclic Redundancy Check) encoding and decoding, optimized for the TI-nspire CX II-T calculator.

## CRC Encoder

`crcEncoder.py` performs CRC encoding on binary data. It divides the data by a generator polynomial and appends the resulting CRC checksum to the original data.

### Customization

- Change `val1` for the data to be encoded.
- Change `val2` for the generator polynomial.

### Use on TI-nspire CX CAS
Download the .py and .tns files from the repository.
Transfer these files to your calculator using the TI-nspire CX CAS Student Software.
Open the files on the calculator to run the scripts.
For more details on the use and customization of the scripts, see the comments in the code.

### Detailed Calculation Output
The crcEncoder.py script not only outputs the Transmitted Value but also shows the entire solution path of the binary polynomial division. This includes each step of the division, the XOR operations, and the calculated remainder. This detailed output helps to better understand and follow the CRC encoding process.

#Author:
@brodbeckleon
@DurrerSimon

### Example

```python
val1 = "011000100101" # Your data
val2 = "10011"       # Your generator polynomial
CRC Decoder
crcDecoder.py is used to verify the integrity of the received data.

