import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image } from 'react-native';
import React, { useEffect, useState } from 'react';

const App = () => {
  const [data, setData] = useState([]);

    const fetchData = async () => {
        try {
            const response = await fetch('http://192.168.0.153:5000/track?name=innerbloom');
            const data = await response.json();
            setData(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    useEffect(() => {
        fetchData();   

    }, []);

  return (
    <View style={styles.container}>
      <Text>{data.name}</Text>
      <Text>{data.artist}</Text>
      <Text>{data.image}</Text>
      <StatusBar style='auto'/>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;
