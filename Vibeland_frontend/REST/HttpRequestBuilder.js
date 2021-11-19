import axios from 'axios';

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