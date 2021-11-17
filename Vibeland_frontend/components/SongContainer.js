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

const SongContainer = (props) => {

    return (
        <FlatList data={ props.songs } renderItem={renderItem}/>
    );
}

export {
    SongContainer
}