import { FlatList, useSafeArea, View, Button, Center, VStack, HStack } from "native-base";
import React, { useEffect, useState } from "react";
import { Text, StyleSheet, ActivityIndicator } from "react-native"
import { SuggestionContainer } from "../components/SuggestionContainer";
import { sendPostRequest } from '../REST/HttpRequestBuilder';
import { MY_USERNAME, ROUTE_TO_SPOTIFY_CONNECTION } from '../constants/constants';
import { flex, justifyContent, marginBottom, style, styles } from "styled-system";
import { MainFeed } from "../components/MainFeed";

const explorePageStyle = StyleSheet.create({
    content: {
        alignItems: 'center',
        flex: 0.8
    },
    exploreButton: {
        marginRight: 15
    },
    statsButton: {
        marginTop: 25
    },
    clearButton: {
        backgroundColor: 'red'
    },
    buttonBox: {
        marginBottom: 15,
        marginTop: 15
    }
});

//This component will contain the home page, from which the user can request song recommendations and view them in a list
const ExplorePage = ({ route, navigation }) => {
    const [username, setUsername] = useState(/*route.params["username"]*/"");
    const [explorePressed, setExplorePressed] = useState(false);
    const [clearPressed, setClearPressed] = useState(false);
    const [authToken, setAuthToken] = useState(undefined);
    const [feedToken, setFeedToken] = useState(undefined);
    const [userFeed, setUserFeed] = useState(undefined);
    const [showSongs, setShowSongs] = useState(false);
    const [loading, setLoading] = useState(false);
    const [songs, setSongs] = useState(undefined);

    //This hook is to make sure the song display conditional is updated appropriately
    useEffect(() => {
        if (songs !== undefined) {
            setShowSongs(true);
        }
        else {
            setShowSongs(false);
        }
    });
        
    //If the user presses the 'Clear' button, clear the list of songs 
    function onPressClear() {
        setExplorePressed(false);
        setShowSongs(false);
        setSongs(undefined);
    }

    //When the user presses the 'Explore' button, send a post request to the backend to retrieve the recommendations
    function onPressExplore() {
        setExplorePressed(true);
        setLoading(true);
        let body = {
            type: "explore",
            credentials: {
                username: username
            }
        }

        //Construct a POST request to be sent to the backend that initiates the song recommendation process
        sendPostRequest(body, ROUTE_TO_SPOTIFY_CONNECTION).then(response => {
            setLoading(false);
            setSongs(response.data["songs"]);
            setAuthToken(response.data["token"]);
            setUserFeed(response.data["user_feed"]);
            setFeedToken(response.data["feed_token"]);
        })
        .catch(error => console.log(error));
    }

    function onPressStats() {
        navigation.navigate('StatsPage', {

        });
    }

    //This function navigates the user to a web page, within the app, to the given URL
    function navigateToSongLink(url, preview) {

        navigation.navigate('SongWebPage', {
            url: url,
            preview: preview
        })
    }

    //This turns off the loading indicator
    function stopLoadingIndicator() {
        setLoading(false);
    }

    return (
        <View style={explorePageStyle.content}>
            <VStack>
                <Center>
                    <HStack style={explorePageStyle.buttonBox}>
                        <Button style={explorePageStyle.exploreButton} onPress={onPressExplore}>
                            Explore Music
                        </Button>
                        { 
                            explorePressed ? 
                            <Button style={explorePageStyle.clearButton} onPress={onPressClear}> 
                                Clear 
                            </Button> : null 
                        }
                    </HStack>
                </Center>
                { 
                    showSongs === true && loading === false &&
                    <Center>
                        <SuggestionContainer 
                            songs={songs}
                            feed={userFeed}
                            show={showSongs}
                            username={username}
                            feedToken={feedToken}
                            authToken={authToken}
                            loading={stopLoadingIndicator}
                            navigation={navigateToSongLink}
                        />
                        {/* <Button style={explorePageStyle.statsButton} onPress={onPressStats}>
                            View Stats
                        </Button> */}
                    </Center>
                }
                {
                    explorePressed === true && loading === true ?
                    <ActivityIndicator size="large"/> : <View/>
                }
            </VStack>
        </View>
    );
}

export {
    ExplorePage
};