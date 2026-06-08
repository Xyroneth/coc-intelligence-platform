"use client";

import { useState } from "react";
import api from "../lib/api";

export default function Home() {
  const [playerTag, setPlayerTag] = useState("");
  const [clanTag, setClanTag] = useState("");

  const [player, setPlayer] = useState<any>(null);
  const [clan, setClan] = useState<any>(null);

  const searchPlayer = async () => {
    try {
      const res = await api.get(`/player/${playerTag}`);
      setPlayer(res.data);
    } catch (error) {
      console.error(error);
      alert("Player not found");
    }
  };

  const searchClan = async () => {
    try {
      const res = await api.get(`/clan/${clanTag}`);

      console.log("CLAN DATA:", res.data);

      setClan(res.data);
    } catch (error) {
      console.error(error);
      alert("Clan not found");
    }
  };

  return (
    <main style={{ padding: "30px" }}>
      <h1>CoC Intelligence Platform</h1>

      <h2>Player Search</h2>

      <input
        value={playerTag}
        onChange={(e) => setPlayerTag(e.target.value)}
        placeholder="Enter Player Tag"
      />

      <button onClick={searchPlayer}>Search Player</button>

      {player && (
        <div>
          <h3>{player.name}</h3>
          <p>Tag: {player.tag}</p>
          <p>Town Hall: {player.townHallLevel}</p>
          <p>Trophies: {player.trophies}</p>
          <p>XP Level: {player.expLevel}</p>
        </div>
      )}

      <hr />

      <h2>Clan Search</h2>

      <input
        value={clanTag}
        onChange={(e) => setClanTag(e.target.value)}
        placeholder="Enter Clan Tag"
      />

      <button onClick={searchClan}>Search Clan</button>

      {clan && (
        <div>
          <h3>{clan.name}</h3>
          <p>Tag: {clan.tag}</p>
          <p>Level: {clan.clanLevel}</p>
          <p>Members: {clan.members}</p>
          <p>War Wins: {clan.warWins}</p>
        </div>
      )}
    </main>
  );
}