"use client";

import { useState } from "react";
import api from "../lib/api";

export default function Home() {
  const [playerTag, setPlayerTag] = useState("");
  const [player, setPlayer] = useState<any>(null);

  const [clanTag, setClanTag] = useState("");
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
      setClan(res.data);
    } catch (error) {
      console.error(error);
      alert("Clan not found");
    }
  };

  return (
    <div
      style={{
        backgroundColor: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1>🛡️ CoC Intelligence Platform</h1>

      <hr />

      <h2>Player Search</h2>

      <input
        value={playerTag}
        onChange={(e) => setPlayerTag(e.target.value)}
        placeholder="Enter Player Tag"
        style={{
          padding: "10px",
          width: "250px",
          color: "black",
        }}
      />

      <button
        onClick={searchPlayer}
        style={{
          marginLeft: "10px",
          padding: "10px",
        }}
      >
        Search Player
      </button>

      {player && (
        <div
          style={{
            marginTop: "20px",
            backgroundColor: "#1e293b",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          <h2>{player.name}</h2>

          <p>Tag: {player.tag}</p>

          <p>Town Hall: {player.townHallLevel}</p>

          <p>Trophies: {player.trophies}</p>

          <p>XP Level: {player.expLevel}</p>
        </div>
      )}

      <hr style={{ marginTop: "40px" }} />

      <h2>Clan Search</h2>

      <input
        value={clanTag}
        onChange={(e) => setClanTag(e.target.value)}
        placeholder="Enter Clan Tag"
        style={{
          padding: "10px",
          width: "250px",
          color: "black",
        }}
      />

      <button
        onClick={searchClan}
        style={{
          marginLeft: "10px",
          padding: "10px",
        }}
      >
        Search Clan
      </button>

      {clan && (
        <>
          <div
            style={{
              marginTop: "20px",
              backgroundColor: "#1e293b",
              padding: "25px",
              borderRadius: "12px",
            }}
          >
            <div
              style={{
                display: "flex",
                gap: "20px",
                alignItems: "center",
              }}
            >
              <img
                src={clan.badgeUrls?.medium}
                alt="Clan Badge"
                width={120}
              />

              <div>
                <h2>{clan.name}</h2>

                <p>{clan.tag}</p>

                <p>{clan.description}</p>
              </div>
            </div>
          </div>

          <h2 style={{ marginTop: "30px" }}>
            📊 Clan Analytics
          </h2>

          <div
            style={{
              display: "grid",
              gridTemplateColumns:
                "repeat(auto-fit, minmax(220px, 1fr))",
              gap: "15px",
              marginTop: "15px",
            }}
          >
            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
                textAlign: "center",
              }}
            >
              <h3>👥 Members</h3>
              <h1>{clan.members}</h1>
            </div>

            <div

            style={{
                backgroundColor: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
                textAlign: "center",
              }}
            >
              <h3>🏆 Clan Level</h3>
              <h1>{clan.clanLevel}</h1>
            </div>

            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
                textAlign: "center",
              }}
            >
              <h3>⚔️ War Wins</h3>
              <h1>{clan.warWins}</h1>
            </div>

            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
                textAlign: "center",
              }}
            >
              <h3>🔥 Win Streak</h3>
              <h1>{clan.warWinStreak}</h1>
            </div>
          </div>
        </>
      )}
    </div>
  );
}