 import { View } from "native-base";
import React from "react";
 import { WebView } from "react-native-webview";

 //This component contains the component that will navigate the user to the Spotify song page using the given URL
 const SongWebPage = ({ route, navigation }) => {
    return (
        <WebView source={{ uri: route.params['url'] }} />
    );
 }

 export {
     SongWebPage
 }