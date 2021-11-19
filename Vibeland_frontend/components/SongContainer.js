import { View, FlatList, VStack, Box, Text, HStack, Avatar, Spacer, Wrap, Pressable } from "native-base";
import { sendGetRequest } from "../REST/HttpRequestBuilder";
import React, { useEffect, useState } from "react";
import { SongWebPage } from "../pages/SongWebPage";
import { WebView } from 'react-native-webview'
import { StyleSheet } from "react-native"
import { NavigationContainer } from "@react-navigation/native";

const songContainerStyles = StyleSheet.create({
    songContainer: {

    },
    songTitle: {
        flexShrink: 1
    }
});

const keyExtractor = (item, index) => index.toString();

function onPressSuggestion(url, preview, props) {
    props.navigation(url, preview);
}

const SongItem = ({ title, artist, art }) => (
    <Wrap flexDirection="row">
        <HStack>
            <Avatar 
                size="48px"
                source={{
                    uri: art
                }}
                marginRight={ 3.5 }
            />
            <VStack>
                <HStack style={{flexDirection:'row'}}>
                    <Text _dark={{
                        color: "warmGray.50",
                        }}
                        color="coolGray.800"
                        bold
                    >
                        Track:
                    </Text>
                    <Text> {title} </Text>
                </HStack>
                <HStack>
                    <Text _dark={{
                        color: "warmGray.50",
                        }}
                        color="coolGray.800"
                        bold
                    >
                        Artist:
                    </Text>
                    <Text> {artist} </Text>
                </HStack>
            </VStack>
        </HStack>
    </Wrap>
);

const renderItem = ({ item }, props) => (
    <VStack>
        <Pressable onPress={() => onPressSuggestion(item.songurl, item.songprev, props)}>
            {({ isPressed }) => {
                return (
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
                        <SongItem title={item.title} artist={item.artists} art={item.coverart} />
                    </Box>
                );
            }
            }
        </Pressable>
    </VStack>
);

const SongContainer = (props) => {
    const [showSongs, setShowSongs] = useState(props.show);
    const [data, setData] = useState(props.songs);

    return (
        <>
            {
                showSongs ?
                    <FlatList
                        keyExtractor={keyExtractor}
                        data={data}
                        renderItem={(item) => renderItem(item, props)}
                        marginTop={15}
                    />
                    : <Text>YAY</Text>
            }
        </>
    );
}

export {
    SongContainer
}