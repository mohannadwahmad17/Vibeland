import axios from 'axios';

//Create a POST request to send the input to the given URL
async function sendPostRequest(input, URL) {
    return await axios({
        method: "POST",
        url: URL,
        data: input,
        headers: {
            "content-type": "application/json"
        }
    });
}

//Create a GET request sent to the given URL
async function sendGetRequest(URL) {
    return await axios({
        method: "GET",
        url: URL,
        headers: {
            "content-type": "application/json"
        }
    });
}

export {
    sendPostRequest,
    sendGetRequest
};