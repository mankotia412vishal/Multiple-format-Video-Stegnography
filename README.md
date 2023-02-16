# Multiple-format-Video-Stegnography
This Is a Video Steganography project contains multiple format

# Tested On :
 
- Ubuntu 

## Features
 
- Encrypt and Encode Text In Video.
- Encrypt and Encode Video In Video.
- Encrypt and Encode Audio In Video.
- Encrypt and Encode Images In Video.
- Encrypt and Encode Text document In Video.
- Encrypt and Encode all format of data together too In Video.
- Decode and Decrypt all these format  From Video.
- Choose AES-256 or RSA Encryption.
- Apply RSA Encryption For AES key.
- Choose Any Frame Number.
- Encrypt Frame Numbers With AES or RSA.
- Save Encrypted Frame Numbers Inside Another Image like Image.png , The Encryoted Image Will Be Stored As Image-enc.png .
### Example for Frame Numbers Hidden Inside Image :
Below encrypted image has ENCRYPTED frame numbers ``` doU2TMGlPJuGcuW5oAIM0LwyWNdaAL8DUJBFmL71LUwXxHvTnP4fS3t72GS0ysDXyPw2TIQnLG7n2ZQ7ePSvBPVuVDkoCBrSR1sriGIXNQg= ``` hidden inside it.
| Original Image | Encrypted Image With Frame Numbers | 
| :---:   | :---: |
| <img style="border-width:0" src="https://raw.githubusercontent.com/Akshay-Arjun/Video-Steganography/main/image.png" width="200"/> | <img style="border-width:0" src="https://raw.githubusercontent.com/Akshay-Arjun/Video-Steganography/main/image-enc.png" width="200"/>   |

## Cracking Keys ?

### AES-256 Breaking :  
- Takes 27,337,893 trillion trillion trillion trillion years to bruteforce key using single computer.
- Takes 13,689 trillion trillion trillion trillion years to bruteforce key using all computers in the world.
### RSA-5000 Breaking :
- 2^1024 / (5.000.000 * 16 * 60 * 60 * 24 * 365) Years to compute the key using brute force, which is about 10^292 years to break RSA-1024.
- We use RSA-5000,I leave it to your imagination on long it takes to break RSA.
## Installation

1 ) Clone project with git

2 ) Go to the directory & install requirements 
```bash
pip install -r requirements.txt
```
3 ) Install FFmpeg </br>
   [Changes depending on the operating system you are using.](https://ffmpeg.org/download.html) </br>
   For Linux & WSL use :
```bash
sudo apt install ffmpeg -y
```
4 ) Create RSA keys.
```bash
python3 rsagen.py
```


## Usage/Examples
1 ) Encryption & Encoding
```bash
python3 encode.py <video-to-encode-with-extension>
```
  Example: 
  ```
  python3 encode.py srutest.mp4
  ```

2 ) Decoding & Decryption
```bash
python3 decode.py <video-to-decode-with-extension>
```
  Example: 
  ```
  python3 decode.py video.mov
  ```
 
