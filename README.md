# BladeLink

![BladeLink Logo](https://github.com/yhnx/BladeLink/blob/main/app/transmitter/src/bladeLINK.png)

*A robust file transmission and reception platform by Team TeleLink.*

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

1. Clone the repository:
   ```bash
   git clone https://github.com/yhnx/BladeLink.git
   cd a
   ```

2. Install GNU Radio: Follow the official GNU Radio installation guide for your platform.

3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Transmitter Application

1. Run the transmitter application:
   ```bash
   python app.py
   ```

2. Follow the on-screen instructions to select and send files.

### Receiver Application

1. The receiver starts automatically and listens for incoming files. Ensure the `rx.py` script is running:
   ```bash
   python rx.py
   ```

2. Received files will be saved in the current directory.

## Project Structure

- `app.py`: Main GUI application for transmission
- `rx.py`: Backend script for file reception
- `requirements.txt`: Lists Python dependencies for the project

## Team TeleLink

*Creators of BladeLink, driving innovation in secure data communication.*

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to GNU Radio and the open-source community for providing excellent tools and support.
