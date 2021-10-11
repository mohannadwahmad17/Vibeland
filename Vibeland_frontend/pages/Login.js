import * as React from 'react';
import { MaterialCommunityIcons, Ionicons } from '@expo/vector-icons';
import {
  NativeBaseProvider,
  Box,
  Text,
  Heading,
  VStack,
  FormControl,
  Input,
  Link,
  Button,
  Icon,
  IconButton,
  HStack,
  Divider,
} from 'native-base';
import { useState, useEffect } from 'react';
import { ROUTE_TO_SPOTIFY_CONNECTION } from '../constants/constants';
import { sendPostRequest } from '../REST/HttpRequestBuilder';
import axios from 'axios';

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  function onUsernameEntered(input) {
    setUsername(input);

    console.log(input)
  }

  function onPressSignIn() {
    
    if (username == "") {
      
      return;
    }

    let headers = {
      accept: 'application/json', 
      contentType: 'application/json'
    };
    let body = {
      credentials : {
        username: username,
        password: password
      }
    }

    sendPostRequest(body, ROUTE_TO_SPOTIFY_CONNECTION).then(response => {
      console.log(response);
    })
    .catch(error => console.log(error));
  }

  return (
    <NativeBaseProvider>
      <Box safeArea flex={1} p="2" py="8" w="90%" mx="auto">
        <Heading size="lg" fontWeight="600" color="coolGray.800">
          Welcome
        </Heading>
        <Heading mt="1" color="coolGray.600" fontWeight="medium" size="xs">
          Sign in to continue!
        </Heading>

        <VStack space={3} mt="5">
          <FormControl>
            <FormControl.Label
              _text={{
                color: 'coolGray.800',
                fontSize: 'xs',
                fontWeight: 500,
              }}>
              Username
            </FormControl.Label>
            <Input onChangeText={onUsernameEntered}/>
          </FormControl>
          <FormControl>
            <FormControl.Label
              _text={{
                color: 'coolGray.800',
                fontSize: 'xs',
                fontWeight: 500,
              }}>
              Password
            </FormControl.Label>
            <Input type="password" />
            <Link
              _text={{ fontSize: 'xs', fontWeight: '500', color: 'indigo.500' }}
              alignSelf="flex-end"
              mt="1">
              Forget Password?
            </Link>
          </FormControl>
          <Button onPress={onPressSignIn} mt="2" colorScheme="indigo" _text={{ color: 'white' }}>
            Sign in
          </Button>
          <HStack mt="6" justifyContent="center">
            <Text fontSize="sm" color="muted.700" fontWeight={400}>
              I'm a new user.{' '}
            </Text>
            <Link
              _text={{
                color: 'indigo.500',
                fontWeight: 'medium',
                fontSize: 'sm',
              }}
              href="#">
              Sign Up
            </Link>
          </HStack>
        </VStack>
      </Box>
    </NativeBaseProvider>
  );
};

export {
  LoginPage
};