import React from 'react';
import { motion } from 'framer-motion';
import { Brain, MessageSquare, Zap, Shield, Clock, BarChart3 } from 'lucide-react';
import FeatureCard from './FeatureCard';

const Features = () => {
  const features = [
    {
      icon: <Brain className="w-6 h-6" />,
      title: "Intelligent AI",
      description: "Powered by advanced AI models to understand and respond with human-like accuracy."
    },
    {
      icon: <MessageSquare className="w-6 h-6" />,
      title: "Natural Conversations",
      description: "Engage in natural, flowing conversations that feel like talking to a real expert."
    },
    {
      icon: <Zap className="w-6 h-6" />,
      title: "Lightning Fast",
      description: "Get instant responses with minimal latency for a seamless experience."
    },
    {
      icon: <Shield className="w-6 h-6" />,
      title: "Enterprise Security",
      description: "Your data is encrypted and secure with enterprise-grade authentication."
    },
    {
      icon: <Clock className="w-6 h-6" />,
      title: "Conversation Memory",
      description: "AI remembers context and preferences for personalized conversations."
    },
    {
      icon: <BarChart3 className="w-6 h-6" />,
      title: "Smart Analytics",
      description: "Track interactions, get insights, and measure performance with analytics."
    }
  ];

  return (
    <section className="py-20 px-4" id="features">
      <div className="container mx-auto max-w-6xl">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl font-bold text-white mb-4">
            Powerful Features for <span className="bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">Modern Teams</span>
          </h2>
          <p className="text-gray-300 max-w-2xl mx-auto">
            Everything you need to build intelligent, context-aware AI applications.
          </p>
        </motion.div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <FeatureCard
              key={index}
              icon={feature.icon}
              title={feature.title}
              description={feature.description}
              delay={index * 0.1}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;