import { FlatList, useSafeArea, View, Button, Center } from "native-base";
import React, { useEffect, useState } from "react";
import { Text } from "react-native"
import { SongContainer } from "../components/SongContainer";
import { sendPostRequest } from '../REST/HttpRequestBuilder';
import { MY_USERNAME, ROUTE_TO_SPOTIFY_CONNECTION } from '../constants/constants';
import { flex, justifyContent, marginBottom, styles } from "styled-system";

const ExplorePage = ({ route, navigation }) => {
    const [username, setUsername] = useState(route.params["username"]);
    const [songs, setSongs] = useState();
    const [explorePressed, setExplorePressed] = useState(false);

    function onPressExplore() {
        setExplorePressed(true);
        let body = {
            type: "explore",
            credentials: {
                username: username
            }
        }

        sendPostRequest(body, ROUTE_TO_SPOTIFY_CONNECTION).then(response => {
            // navigation.navigate('SongContainer', { song_list: response.data["songs"] });
            setSongs(response.data["songs"]);
            console.log(songs)
        })
        .catch(error => console.log(error));
    }

    return (
        <>
            <View style={{ justifyContent: 'flex-start', flex: 1 }} >
                <Center flex={1} px="3">
                    <Button onPress={onPressExplore}>
                        Explore Music
                    </Button>
                </Center>
            </View>
            <View>
                {/* {explorePressed? <SongContainer songs={songs}/> : <View/>} */}
                <SongContainer songs={songs}/>
            </View>
        </>
    );
}

export {
    ExplorePage
};