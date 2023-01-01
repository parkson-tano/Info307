import { View, Text, StyleSheet } from 'react-native'
import React from 'react'
import { Card, ListItem, Button, Icon } from "react-native-elements";
import BootstrapStyleSheet from 'react-native-bootstrap-styles';
import { useNavigation } from "@react-navigation/native";
const bootstrapStyleSheet = new BootstrapStyleSheet();
const { s, c } = bootstrapStyleSheet;

const Balance = () => {
  const navigation = useNavigation();
  const fxn = () => {
   navigation.navigate("Transaction");
  }
  return (
    <View style={[s.container]}>
      <Card>
        <Card.Title>XAF 450,00</Card.Title>
        <Card.Divider />
        <View>
          <View style={styles.container}>
            <View style={styles.item1}>
              <Text
                style={{
                  fontSize: 25,
                  fontWeight: "bold",
                  marginBottom: 5,
                }}
              >
                Last Transaction
              </Text>
            </View>
            <View style={styles.item2}>
              <Button
                buttonStyle={{
                  borderRadius: 0,
                  marginLeft: 0,
                  marginRight: 0,
                  marginBottom: 0,
                }}
                title="See More"
                type="clear"
                onPress={fxn}
              />
            </View>
          </View>

          <View style={styles.container}>
            <View style={styles.item1}>
              <Text style={[s.text, s.h3, s.textPrimary]}>{"Deposit"}</Text>
              <Text style={[s.text, s.h5, s.textPrimary]}>{"674128573"}</Text>
            </View>
            <View style={styles.item2}>
              <Text style={[s.text, s.h5]}>{"-2444"}XAF</Text>
              <Text style={[s.text, s.h5]}>{"4:34PM"}</Text>
            </View>
          </View>
        </View>
      </Card>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    flexWrap: "wrap",
    alignItems: "flex-start", // if you want to fill rows left to right
  },
  item1: {
    width: "70%",
    marginVertical: 10,
    // is 50% of container width
  },
  item2: {
    width: "30%",
    marginVertical: 10,
    // is 50% of container width
  },
});

export default Balance