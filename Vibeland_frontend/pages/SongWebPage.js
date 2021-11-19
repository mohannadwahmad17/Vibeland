 import { View } from "native-base";
import React from "react";
 import { WebView } from "react-native-webview";

 const SongWebPage = ({ route, navigation }) => {
    console.log(route.params['url'])
    return (
        <WebView source={{ uri: route.params['url'] }} />
    );
 }

 export {
     SongWebPage
 }