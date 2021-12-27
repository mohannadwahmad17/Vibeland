import React from "react";
import { View, FlatList, VStack, Box, Text, HStack, Avatar, Spacer, Wrap, Pressable } from "native-base";

//This componenet represents a song item that displays a song's name, artist name, and the album cover art
const SongItem = (props) => (
    <Wrap flexDirection="row">
        <HStack>
            <Avatar 
                size="48px"
                source={{
                    uri: props.art
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
                    <Text> {props.title} </Text>
                </HStack>
                {/* <HStack>
                    <Text _dark={{
                        color: "warmGray.50",
                        }}
                        color="coolGray.800"
                        bold
                    >
                        Artist:
                    </Text>
                    <Text> {props.artistName} </Text>
                </HStack> */}
                <HStack>
                    <Text _dark={{
                        color: "warmGray.50",
                        }}
                        color="coolGray.800"
                        bold
                    >
                        Genre:
                    </Text>
                    <Text> {props.genre} </Text>
                </HStack>
            </VStack>
        </HStack>
    </Wrap>
);

export {
    SongItem
}