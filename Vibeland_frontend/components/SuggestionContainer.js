import { View, FlatList, VStack, Box, Text, HStack, Avatar, Spacer, Wrap, Pressable } from "native-base";
import { NavigationContainer } from "@react-navigation/native";
import { sendGetRequest } from "../REST/HttpRequestBuilder";
import { SongPreviewPlayer } from "./SongPreviewPlayer";
import React, { useEffect, useState } from "react";
import { SongWebPage } from "../pages/SongWebPage";
import { WebView } from 'react-native-webview'
import { StyleSheet, Dimensions } from "react-native"
import { SongItem } from "./SongItem";
import { MainFeed } from "./MainFeed";

//Define the styles for the different components in a song container
const songContainerStyles = StyleSheet.create({
    songContainer: {
        width: Dimensions.get('window').width * 0.95
    },
    songFlatList: {
        borderRadius: 15,
        overflow: 'hidden',
        marginTop: 15,
        marginBottom: 15
    },
    shadowProp: {
        shadowColor: '#171717',
        shadowOffset: {width: -2, height: 4},
        shadowOpacity: 0.2,
        shadowRadius: 3,
    },
    songTitle: {
        flexShrink: 1
    },
    headerText: {
        fontWeight: 'bold',
        fontSize: 20,
        color: '#0078ff',
        fontFamily: 'Helvetica Neue',
        textAlign: 'left',
        marginLeft: 10
    }
});

const keyExtractor = (item, index) => index.toString();

//This represents the item to be rendered in a flatlist
const RenderItem = (props) => {

    //Navigate the user to the song web page upon tapping on the item
    function onPressSuggestion(props) {
        props.navigation(props.item.songurl, props.item.songprev);
    }

    return (
        <VStack>
            { /* Render item must be pressable to navigate user to the associated Spotify song web page */ }
            <Pressable onPress={() => onPressSuggestion(props)}>
                {
                    ({ isPressed }) => {
                        return (
                            props.songTier === props.item.tier &&
                            <Box
                                bg={isPressed ? "coolGray.200" : "white"}
                                borderBottomWidth="1"
                                _dark={{
                                    borderColor: "gray.600",
                                }}
                                borderColor="coolGray.200"
                                pl="4"
                                pr="5"
                                py="2"
                            >
                                { /* Render the song item containing the song title, artist name, and album cover art */ }
                                <SongItem 
                                    title={props.item.title} 
                                    artist={props.item.artists} 
                                    art={props.item.coverart}
                                    genre={props.item.genre}
                                />
                            </Box>
                        );
                    }
                }
            </Pressable>
        </VStack>
    )
}

//This tier container is a list of song recommendations for a particular tier
//Tiers are:
// 1. Most likely for the user to like
// 2. Similar songs but different enough
// 3. Very new songs that the application suggests to encourage exploration
const TierContainer = (props) => {
    return (
        <>
            <View>
                <Text style={songContainerStyles.headerText}>
                    { props.header }
                </Text>
            </View>
            <View style={songContainerStyles.shadowProp}>
                <FlatList
                    style={songContainerStyles.songFlatList}
                    keyExtractor={keyExtractor}
                    data={props.data}
                    renderItem={
                        ({ item }) => <RenderItem
                            navigation={props.navigation}
                            item={item}
                            setUris={props.setUris}
                            spotifyAccessor={props.props}
                            setShowPlayer={props.setShowPlayer}
                            setSongPreviewLink={props.setSongPreviewLink}
                            songTier={props.songTier}
                        />
                    }
                />
            </View>
        </>
    );
}

//List of metadata defining the different song recommendation tier lists
const lists = [
    { id: 0, title: "More of your Favorites:", tier: "rec1" },
    { id: 1, title: "Similar to you Favorites:", tier: "rec2" },
    { id: 2, title: "Explore Something New:", tier: "rec3" }
]

//This represents the component that contains the scrollable flatlist with all the song items 
const SuggestionContainer = (props) => {
    const [songPreviewLink, setSongPreviewLink] = useState();
    const [feedToken, setFeedToken] = useState(props.feedToken);
    const [userFeed, setUserFeed] = useState(props.userFeed);
    const [authToken, setToken] = useState(props.authToken);
    const [showRecs, setShowRecs] = useState(props.show);
    const [showPlayer, setShowPlayer] = useState(false);
    const [data, setData] = useState(props.songs);
    const [uris, setUris] = useState();

    useEffect(() => {
        if (showRecs) {
            props.loading();
        }
    });

    return (
        // <VStack>
        //     {
        //         /* If the songs are available to show, render a scrollable flatlist containing all the song items */
        //         showRecs ?
        //             <FlatList
        //                 style={songContainerStyles.songContainer}
        //                 keyExtractor={keyExtractor}
        //                 data={lists}
        //                 renderItem={
        //                     ({ item }) => 
        //                         <TierContainer
        //                             data={data}
        //                             setUris={setUris}
        //                             header={item.title}
        //                             songTier={item.tier}
        //                             spotifyAccessor={props}
        //                             username={props.username}
        //                             navigation={props.navigation}
        //                             setShowPlayer={setShowPlayer}
        //                             setSongPreviewLink={setSongPreviewLink}
        //                         />
        //                 }
        //             />
        //         : <Text>YAY</Text>
        //     }
        // </VStack>
        <MainFeed 
            navigation={props.navigation}
            songRecommendations={data} 
            showRecs={showRecs}
        />
    );
}

export {
    SuggestionContainer
}