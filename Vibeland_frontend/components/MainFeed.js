import { FlatList, View, Text } from 'native-base';
import React, { useEffect, useState } from 'react';
import { STREAM_API_ID, STREAM_API_KEY } from '../constants/constants';
import { SongRecItem } from './SongRecItem';
import { StyleSheet, Dimensions } from 'react-native';

const mainFeedStyles = StyleSheet.create({
    recContainer: {
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
});

const keyExtractor = (item, index) => index.toString();

const MainFeed = (props) => {
    const [appId, setAppId] = useState(STREAM_API_ID);
    const [token, setToken] = useState(props.feedToken);
    const [userId, setUserId] = useState(props.username);
    const [apiKey, setApiKey] = useState(STREAM_API_KEY);
    const [showRecs, setShowRecs] = useState(props.showRecs);
    const [recData, setRecData] = useState(props.songRecommendations);

    return (
        <View style={mainFeedStyles.shadowProp}>
            { showRecs ?
                <FlatList
                    style={mainFeedStyles.recContainer}
                    keyExtractor={keyExtractor}
                    data={recData}
                    renderItem={
                        ({ item }) => <SongRecItem
                            artistImage={item.artistImage}
                            navigation={props.navigation}
                            artistName={item.artists}
                            albumArt={item.coverart}
                            songTitle={item.title}
                            songUrl={item.songurl}
                            genre={item.genre}
                        />
                    }
                />
                : <View/>
            }
        </View>
    );
}

export {
    MainFeed
}