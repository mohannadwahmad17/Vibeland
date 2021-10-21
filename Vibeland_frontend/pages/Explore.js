import { FlatList, List, View } from "native-base";
import React, { useState } from "react";
import { Text } from "react-native"

const default_list = [
    {
        "title": "Default"
    }
]

const Song = ({ title }) => (
    <View>
        <Text>{title}</Text>
    </View>
);

const renderItem = ({ item }) => (
    <Song title={item.title} />
);

const ExplorePage = ({ navigation }) => {
    const [songs, setSongs] = useState(default_list);

    return (
        <List>
            <FlatList data={songs} renderItem={renderItem}/>
        </List>
    );
}

export {
    ExplorePage
};