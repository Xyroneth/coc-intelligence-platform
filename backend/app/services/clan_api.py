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
      const res = await api.get(/player/${playerTag});
      setPlayer(res.data);
    } catch (error) {
      console.error(error);
      alert("Player not found");
    }
  };

  const searchClan = async () => {
    try {
      const res = await api.get(/clan/${clanTag});
      setClan(res.data);
    } catch (error) {
      console.error(error);
      alert("Clan not found");
    }
  };

  const members = clan?.memberList || [];

  const avgXP =
    members.length > 0
      ? Math.round(
          members.reduce(
            (sum: number, m: any) => sum + m.expLevel,
            0
          ) / members.length
        )
      : 0;

  const avgTH =
    members.length > 0
      ? (
          members.reduce(
            (sum: number, m: any) => sum + m.townHallLevel,
            0
          ) / members.length
        ).toFixed(1)
      : 0;

  const highestXP =
    members.length > 0
      ? [...members].sort(
          (a: any, b: any) => b.expLevel - a.expLevel
        )[0]
      : null;

  const topDonor =
    members.length > 0
      ? [...members].sort(
          (a: any, b: any) => b.donations - a.donations
        )[0]
      : null;

  const leadersAndAdmins = members.filter(
    (m: any) =>
      m.role === "leader" ||
      m.role === "coLeader" ||
      m.role === "admin"
  ).length;

  const topXPPlayers = [...members]
    .sort((a: any, b: any) => b.expLevel - a.expLevel)
    .slice(0, 10);

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
              marginTop: "25px",
              backgroundColor: "#1e293b",
              padding: "25px",
              borderRadius: "15px",
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
                alt="badge"
                width={120}
              />

              <div>
                <h1>{clan.name}</h1>
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
            }}
          >
            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>👥 Members</h3>
              <h2>{clan.members}</h2>
            </div>

            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>🏰 Avg Town Hall</h3>
              <h2>{avgTH}</h2>
            </div>

            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>⭐ Avg XP</h3>
              <h2>{avgXP}</h2>
            </div>

            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>⚔️ War Wins</h3>
              <h2>{clan.warWins}</h2>
            </div>

            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>🔥 Win Streak</h3>
              <h2>{clan.warWinStreak}</h2>
            </div>

            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>👑 Leaders/Admins</h3>
              <h2>{leadersAndAdmins}</h2>
            </div>
          </div>

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 1fr",
              gap: "20px",
              marginTop: "25px",
            }}
          >
            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>🏆 Highest XP Player</h3>

              {highestXP && (
                <>
                  <p>Name: {highestXP.name}</p>
                  <p>XP: {highestXP.expLevel}</p>
                  <p>TH: {highestXP.townHallLevel}</p>
                </>
              )}
            </div>

            <div
              style={{
                background: "#1e293b",
                padding: "20px",
                borderRadius: "12px",
              }}
            >
              <h3>🎁 Top Donor</h3>

              {topDonor && (
                <>
                  <p>Name: {topDonor.name}</p>
                  <p>Donations: {topDonor.donations}</p>
                  <p>Received: {topDonor.donationsReceived}</p>
                </>
              )}
            </div>
          </div>

          <div
            style={{
              marginTop: "30px",
              backgroundColor: "#1e293b",
              padding: "20px",
              borderRadius: "12px",
            }}
          >
            <h2>🏅 Top 10 XP Players</h2>

            <table
              style={{
                width: "100%",
                marginTop: "10px",
              }}
            >
              <thead>
                <tr>
                  <th align="left">Player</th>
                  <th align="left">Role</th>
                  <th align="left">TH</th>
                  <th align="left">XP</th>
                  <th align="left">Donations</th>
                </tr>
              </thead>

              <tbody>
                {topXPPlayers.map((member: any) => (
                  <tr key={member.tag}>
                    <td>{member.name}</td>
                    <td>{member.role}</td>
                    <td>{member.townHallLevel}</td>
                    <td>{member.expLevel}</td>
                    <td>{member.donations}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  );
}