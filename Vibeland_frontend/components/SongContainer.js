import { View } from "native-base";
import React, { useEffect, useState } from "react";
import { Text, StyleSheet } from "react-native"
import { List, ListItem, FlatList } from "react-native-elements";

const songContainerStyles = StyleSheet.create({
    songContainer: {

    },
    songItem: {

    }
});

const Song = ({ title }) => (
    <View>
        <Text>{title}</Text>
    </View>
);

const keyExtractor = (item, index) => index.toString()

const renderItem = ({ item }) => (
    // <Song title={item.title} />
    <ListItem bottomDivider>

    </ListItem>
);

const renderSeparator = () => {
    return (
        <View
            style={{
                height: 1,
                width: "86%",
                backgroundColor: "#CED0CE",
                marginLeft: "14%"
            }}
        />
    );
};

const SongContainer = (props) => {
    const [showSongs, setShowSongs] = useState(false);
    const [data, setData] = useState(props.songs);

    useEffect(() => {
        console.log(props.songs)
        if (data !== undefined) {
            setShowSongs(true);
        }
    })

    return (
        <>
            {
                showSongs ?
                    <FlatList
                        keyExtractor={keyExtractor}
                        data={props.songs}
                        renderItem={renderItem}
                    />
                    // <Text>HI</Text>
                    : <Text>YAY</Text>
            }
        </>
    );
}

export {
    SongContainer
}