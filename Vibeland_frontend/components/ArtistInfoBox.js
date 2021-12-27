import React, { useEffect, useState } from "react";
import { Avatar, Box, Center, View, VStack, Text } from 'native-base'

//This represents the item containing an artist's information, to be shown in the feed
const ArtistInfoBox = (props) => {
    const [artistImageUrl, setArtistImageUrl] = useState(props.artistImageUrl);
    const [artistInitials, setArtistInitials] = useState(props.artistInitials);
    const [artistName, setArtistName] = useState(props.artistName);

    return (
        <View>
            <Box>
                <VStack>
                    <Center>
                        <Avatar
                            source={{
                                uri: artistImageUrl
                            }}
                        >
                            {artistInitials}
                        </Avatar>
                    </Center>
                    <Center>
                        <Text> {artistName} </Text>
                    </Center>
                </VStack>
            </Box>
        </View>
    );
}

export {
    ArtistInfoBox
}