const axios = require("axios");
const fs = require("fs");
const path = require("path");

async function uploadFile(filePath) {
  try {
    const fileName = path.basename(filePath);
    const fileStream = fs.createReadStream(filePath);

    const response = await axios.post(
      "http://localhost:5000/upload",
      fileStream,
      {
        headers: {
          "Content-Type": "application/octet-stream",
          "X-Filename": fileName,
        },
      }
    );

    console.log("Server response:", response.data);
  } catch (error) {
    console.error(
      "Error uploading file:",
      error.response?.data || error.message
    );
  }
}

uploadFile("all_packages-arm64-7.16.1.zip");
