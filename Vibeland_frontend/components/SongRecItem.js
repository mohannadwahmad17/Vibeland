import { Avatar, Box, Center, View, VStack, Pressable } from 'native-base'
import React, { useEffect, useState } from "react";
import { SongWebPage } from "../pages/SongWebPage";
import { ArtistInfoBox } from "./ArtistInfoBox";
import { StyleSheet } from "react-native";
import { SongItem } from "./SongItem";

const songRecItemStyles = StyleSheet.create({
    recommendationCardStyle: {
        borderRadius: 15,
        overflow: 'hidden',
        marginTop: 10,
        marginBottom: 10,
    },
    shadowProp: {
        shadowColor: '#171717',
        shadowOffset: {width: -3, height: 5},
        shadowOpacity: 1.5,
        shadowRadius: 3.5,
    }
});

//This represents the item containing an artist's information, to be shown in the feed
const SongRecItem = (props) => {
    // const [artistInitials, setArtistInitials] = useState(props.artistName[0]);
    const [artistImageUrl, setArtistImageUrl] = useState(props.artistImage);
    const [artistName, setArtistName] = useState(props.artistName);
    const [songTitle, setSongTitle] = useState(props.songTitle);
    const [albumArt, setAlbumArt] = useState(props.albumArt);
    const [songUrl, setSongUrl] = useState(props.songUrl);
    const [genre, setGenre] = useState(props.genre);

    //Navigate the user to the song web page upon tapping on the item
    function onPressSuggestion(songUrl) {
        props.navigation(songUrl);
    }

    return (
        <View style={songRecItemStyles.recommendationCardStyle}>
            <Box>
                <VStack>
                    <Pressable onPress={() => onPressArtistBox()}>
                        {
                            ({ isPressed }) => {
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
                                        <ArtistInfoBox
                                            artistImageUrl={artistImageUrl}
                                            // artistInitials={artistInitials}
                                            artistName={artistName}
                                        />
                                    </Box>
                                );
                            }
                        }
                    </Pressable>
                    <Pressable onPress={() => onPressSuggestion(songUrl)}>
                        {
                            ({ isPressed }) => {
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
                                        { /* Render the song item containing the song title, artist name, and album cover art */}
                                        <SongItem
                                            artistName={artistName}
                                            title={songTitle}
                                            art={albumArt}
                                            genre={genre}
                                        />
                                    </Box>
                                );
                            }
                        }
                    </Pressable>
                </VStack>
            </Box>
        </View>
    );
}

export {
    SongRecItem
}