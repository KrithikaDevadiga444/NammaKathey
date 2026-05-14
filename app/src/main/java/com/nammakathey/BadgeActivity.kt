package com.nammakathey

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.nammakathey.data.DataProvider
import com.nammakathey.data.UserManager
import com.nammakathey.databinding.ActivityBadgeBinding
import com.nammakathey.model.Hero

class BadgeActivity : AppCompatActivity() {

    private lateinit var binding: ActivityBadgeBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityBadgeBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val currentUser = UserManager.getCurrentUser(this)
        val allHeroes = DataProvider.getDistricts().flatMap { it.heroes }
        
        val earnedBadges = allHeroes.filter { hero ->
            currentUser?.earnedBadges?.contains(hero.id) == true
        }

        binding.rvBadges.layoutManager = LinearLayoutManager(this)
        binding.rvBadges.adapter = BadgeAdapter(earnedBadges)

        binding.btnBack.setOnClickListener {
            finish()
        }
    }

    class BadgeAdapter(private val heroes: List<Hero>) : RecyclerView.Adapter<BadgeAdapter.ViewHolder>() {

        class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
            val tvName: TextView = view.findViewById(R.id.tvBadgeName)
            val tvDistrict: TextView = view.findViewById(R.id.tvDistrictName)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.item_badge, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val hero = heroes[position]
            holder.tvName.text = "${hero.name} Badge"
            
            val district = DataProvider.getDistricts().find { it.heroes.contains(hero) }
            holder.tvDistrict.text = district?.name ?: "Unknown District"
        }

        override fun getItemCount() = heroes.size
    }
}
