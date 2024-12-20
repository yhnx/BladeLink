# BladeLink

![BladeLink Logo](https://github.com/yhnx/BladeLink/blob/main/app/transmitter/src/bladeLINK%20(1).png)

*A robust file transmission and reception platform utilizing Blade RFs by Team TeleLink.*

## Features

- **File Transmission & Reception**: Seamlessly send and receive files
- **User Interface**: Built with `customtkinter` for an interactive and user-friendly experience
- **Encryption Support**: Ensures secure data sharing
- **Real-Time Progress**: Displays live progress during transmission and reception

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- GNU Radio
- BladeRF drivers (if using BladeRF hardware)

### Steps

1. Install GNU Radio: Follow the official GNU Radio installation guide for your platform.
   
2. Clone the repository:
   ```bash
   git clone https://github.com/yhnx/BladeLink.git
   ``` 

4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running BladeLink Application

1. Move to the required directory:
   ```bash
   cd app
   ``` 

2.   Run the transmitter application:
   ```bash
   python app.py
   ```

3. Follow the on-screen instructions to select and send files.



## Project Structure

- `app.py`: Main GUI application for transmission and reception
- `Telelink_reciever.py`: Backend script for file reception (made using GNU Radio)
-  `Telelink_transmitter.py`: Backend script for file transmission (made using GNU Radio)
- `requirements.txt`: Lists Python dependencies for the project

## TeleLink Communications

![Telelink Logo](https://github.com/yhnx/BladeLink/blob/main/app/transmitter/src/telelink_logo.png)

*Creators of BladeLink, driving innovation in secure data communication.*

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request


## Acknowledgments

Special thanks to GNU Radio and the open-source community for providing excellent tools and support.
