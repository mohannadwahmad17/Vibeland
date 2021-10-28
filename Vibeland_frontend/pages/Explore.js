import { FlatList, View } from "native-base";
import React, { useEffect, useState } from "react";
import { Text } from "react-native"

const Song = ({ title }) => (
    <View>
        <Text>{title}</Text>
    </View>
);

const renderItem = ({ item }) => (
    <Song title={item.title} />
);

const ExplorePage = ({ route, navigation }) => {
    const [songs, setSongs] = useState(route.params["song_list"]);

    useEffect(() => {
        console.log(songs);
    }, []);

    return (
        <View>
            <FlatList data={ songs } renderItem={renderItem}/>
        </View>
    );
}

export {
    ExplorePage
};