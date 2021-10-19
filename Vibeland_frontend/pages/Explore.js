import { FlatList, List, View } from "native-base";
import React, { useState } from "react";

const default_list = [
    {
        "song_title" : "Default"
    }
]

const Song = ({title}) => (
    <View>
        <Text>{title}</Text>
    </View>
);

const renderItem = ({ item }) => (
    <Song title={item.title} />
  );

const ExplorePage = () => {
    const [songs, setSongs] = useState(default_list);

    return(
        <List>
            <FlatList 
                data={songs}
                renderItem={renderItem}
            />
        </List>
    );
}