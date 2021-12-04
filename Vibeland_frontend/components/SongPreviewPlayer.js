import { Box, View } from "native-base";
import { StyleSheet } from "react-native"
import { WebView } from "react-native-webview";
import React, { useEffect, useState } from "react";
import { SpotifyPlayer } from "react-spotify-web-playback";

const songPreviewStyle = StyleSheet.create({
    mainContainer: {
        width: '100%',
        height: 50,
        backgroundColor: '#FF9800',
        justifyContent: 'center',
        alignItems: 'center',
        position: 'absolute',
        bottom: 0
    },
});

const SongPreviewPlayer = (props) => {
    const [previewLink, setSongPreviewLink] = useState(props.previewLink);
    const [token, setToken] = useState(props.token);
    const [uris, setUris] = useState(props.uris);

    return (
        <WebView >
        <SpotifyPlayer
            token="BQAI_7RWPJuqdZxS-I8XzhkUi9RKr8Q8UUNaJAHwWlpIq6..."
            uris={['spotify:artist:6HQYnRM4OzToCYPpVBInuU']}
        />
        </WebView>
    );
}

export {
    SongPreviewPlayer
}